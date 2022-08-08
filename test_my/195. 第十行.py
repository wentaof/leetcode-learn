# # cat -n ：cat的时候显示行号
# cat -n file.txt | awk '{if($1==10){print $0}}'|cut -f2
# #
# head -n 10 file.txt|tail -n 1
# #
# sed -n '10p' file.txt
# #
# awk '{if(NR==10){print $0}}' file.txt
# #
# line=`cat file.txt | wc -l`
# if [[ line -ge 10 ]]
# then
#     head -n 10 file.txt | tail -n 1
# else
#     awk '{if($NF==1){print FILENAME}}' file.txt
# fi