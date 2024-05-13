class Hesab:
    def __init__(self, hesab_nomresi: int, balans: float):
        self.hesab_nomresi = hesab_nomresi
        self.balans = balans

    def balansi_artir(self, mebleg: float):
        self.balans += mebleg
        print("Balans artırıldı. Yeni balans:", self.balans)

    def pul_cixar(self, mebleg: float):
        if mebleg > self.balans:
            print("Əsas hesabınızda kifayət qədər pul yoxdur.")
        else:
            self.balans -= mebleg
            print("Pul uğurla çıxarıldı. Yeni balans:", self.balans)

    def balansi_goster(self):
        print("Hesab nömrəsi:", self.hesab_nomresi)
        print("Cari balans:", self.balans)


class Kredit(Hesab):
    def __init__(self, hesab_nomresi: int, balans: float, kredit_meb: float):
        super().__init__(hesab_nomresi, balans)
        self.kredit_meb = kredit_meb

    def kredit_ver(self):
        self.balans += self.kredit_meb
        print("Kredit uğurla götürüldü. Yeni balans:", self.balans)

    def kredit_odenisi(self):
        aylıq_odenis = self.kredit_meb / 12
        if self.balans >= aylıq_odenis:
            self.balans -= aylıq_odenis
            print("Kredit ödənişi uğurla həyata keçirildi. Yeni balans:", self.balans)
        else:
            print("Kredit ödənişi üçün kifayət qədər balans yoxdur.")


hesab1 = Hesab(1001, 500)
hesab1.balansi_goster()

hesab1.balansi_artir(300)
hesab1.balansi_goster()

hesab1.pul_cixar(200)
hesab1.balansi_goster()

kredit1 = Kredit(1002, 1000, 500)
kredit1.balansi_goster()

kredit1.kredit_ver()
kredit1.balansi_goster()

kredit1.kredit_odenisi()
kredit1.balansi_goster()
