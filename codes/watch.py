# s = "df,sgsdf,dfs,fdsfds,fsdf"
# s_s = s.split(",")
#
# print(s_s)


text = input()
# 3 55

text_s = text.split(" ")

hour = 12 - int(text_s[0])
minute = 60 - int(text_s[1])

if hour == 12:
    hour = 0

if minute == 60:
    minute = 0

result_hour = hour
result_minute = minute

if hour < 10:
    result_hour = "0" + str(hour)

if minute < 10:
    result_minute = "0" + str(minute)

print("{}:{}".format(result_hour, result_minute))
