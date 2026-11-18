class StokKurangError(Exception):
  pass


class Pelanggan:

  def __init__(self, nama):
    self.nama = nama

  def diskon(self):
    return 0.0


class MemberVIP(Pelanggan):

  def __init__(self, nama):
    super().__init__(nama)

  def diskon(self):
    return 0.15


class DetailPesanan:

  def __init__(self, menu, porsi):
    if porsi > menu.stok:
      raise StokKurangError(
          f"Stok {menu.nama} tidak mencukupi (Sisa: {menu.stok})!"
      )
    self.menu = menu
    self.porsi = porsi
    menu.stok -= porsi

  @property
  def subtotal(self):
    return self.menu.hitung_harga(self.porsi)


class OrderRestoran:
  PAJAK = 0.10

  def __init__(self, pelanggan, nomor_meja):
    self.pelanggan = pelanggan
    self.nomor_meja = nomor_meja
    self.items = []

  def tambah_item(self, menu, porsi):
    self.items.append(DetailPesanan(menu, porsi))

  def ringkasan_tagihan(self):
    subtotal = sum(i.subtotal for i in self.items)
    potongan = subtotal * self.pelanggan.diskon()
    setelah_diskon = subtotal - potongan
    pajak = setelah_diskon * self.PAJAK
    total_akhir = setelah_diskon + pajak
    return {
        "subtotal": subtotal,
        "diskon": potongan,
        "pajak": pajak,
        "total": total_akhir,
    }
