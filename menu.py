from abc import ABC, abstractmethod


class ItemMenu(ABC):
  total_menu = 0

  def __init__(self, kode, nama, harga, stok):
    self.__kode = kode
    self.__nama = nama
    self.__harga = harga
    self._stok = stok
    ItemMenu.total_menu += 1

  @property
  def kode(self):
    return self.__kode

  @property
  def nama(self):
    return self.__nama

  @property
  def harga(self):
    return self.__harga

  @property
  def stok(self):
    return self._stok

  @stok.setter
  def stok(self, jumlah):
    self._stok = jumlah

  @abstractmethod
  def kategori(self):
    pass

  @abstractmethod
  def hitung_harga(self, porsi):
    pass

  @staticmethod
  def format_rp(angka):
    return f"Rp {angka:,.0f}".replace(",", ".")


class Makanan(ItemMenu):

  def __init__(self, kode, nama, harga, stok, pedas=False):
    super().__init__(kode, nama, harga, stok)
    self.pedas = pedas

  def kategori(self):
    return "Makanan Utama" + (" (Pedas)" if self.pedas else "")

  def hitung_harga(self, porsi):
    return self.harga * porsi


class Minuman(ItemMenu):

  def __init__(self, kode, nama, harga, stok, dingin=True):
    super().__init__(kode, nama, harga, stok)
    self.dingin = dingin

  def kategori(self):
    return "Minuman " + ("Dingin" if self.dingin else "Panas")

  def hitung_harga(self, porsi):
    return self.harga * porsi
