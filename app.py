from flask import Flask, render_template, request
from models.menu import ItemMenu, Makanan, Minuman
from models.transaksi import MemberVIP, OrderRestoran, Pelanggan, StokKurangError

app = Flask(__name__)

daftar_menu = [
    Makanan("M01", "Ramen Spesial Giken", 38000, 10, pedas=True),
    Makanan("M02", "Chicken Katsu Curry", 32000, 12, pedas=False),
    Minuman("D01", "Ocha Dingin", 8000, 30, dingin=True),
]


@app.route("/", methods=["GET", "POST"])
def index():
  error_msg = None
  struk_data = None
  if request.method == "POST":
    nama = request.form.get("nama")
    meja = request.form.get("meja")
    status = request.form.get("status")
    kode_menu = request.form.get("kode_menu")
    porsi = int(request.form.get("porsi", 1))

    pelanggan = MemberVIP(nama) if status == "vip" else Pelanggan(nama)
    order = OrderRestoran(pelanggan, meja)
    menu_terpilih = next(
        (m for m in daftar_menu if m.kode == kode_menu), None
    )

    if menu_terpilih:
      try:
        order.tambah_item(menu_terpilih, porsi)
        tagihan = order.ringkasan_tagihan()
        struk_data = {
            "pelanggan": pelanggan.nama,
            "status": "VIP" if status == "vip" else "Umum",
            "meja": meja,
            "item": menu_terpilih.nama,
            "porsi": porsi,
            "total": ItemMenu.format_rp(tagihan["total"]),
        }
      except StokKurangError as e:
        error_msg = str(e)

  return render_template(
      "index.html", daftar_menu=daftar_menu, error=error_msg, struk=struk_data
  )


if __name__ == "__main__":
  app.run(debug=True)
