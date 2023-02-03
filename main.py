import bevezetes
import sorozat
import autom

bevezetes.auto_kor()
lista = sorozat.otos_szamsor()
sorozat.kiir(lista)
egyjegyu = sorozat.egyjegyuek_szama(lista)
sorozat.konzol_kiir(egyjegyu)
sorozat.file_kiir("szamok.txt", egyjegyu)
auto_lista = autom.fajl_beolvas()
autom.flotta(auto_lista)
autom.legfiatalabb(auto_lista)