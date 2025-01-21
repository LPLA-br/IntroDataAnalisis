ANOTAÇÕES METODOLÓGICAS

VIKING II Utopia planitia

./vl2_tbin.dat é derivado de ./vl_tbin.dat

$ grep '^ VL2' vl_tbin.dat | wc -l
  24750 linhas (entradas)
$ grep '^ VL2' vl_tbin.dat > vl2_tbin.dat

Dados de topografia .dat convertidos para .csv
sed -E 's/ /,/g' topo.dat | sed -E 's/,{2,9}/,/g' | sed -E 's/^,//g' | sed -E 's/$/,/g' > topo.csv 
