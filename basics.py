import datetime
import decimal
x = 10
y = 10

# ########### Some examples of formatted string literals STARTS #############:
name = "Fred"
f"He said his name is {name!r}."

f"He said his name is {repr(name)}."  # repr() is equivalent to !r

width = 10
precision = 4
value = decimal.Decimal("12.34567")
f"result: {value:{width}.{precision}}"  # nested fields

today = datetime(year=2017, month=1, day=27)
f"{today:%B %d, %Y}"  # using date format specifier

f"{today=:%B %d, %Y}"  # using date format specifier and debugging

number = 1024
f"{number:#0x}"  # using integer format specifier

foo = "bar"
f"{ foo = }"  # preserves whitespace

line = "The mill's closed"
f"{line = }"

f"{line = :20}"

f"{line = !r:20}"
# ############# Some examples of formatted string literals ENDS ###########:
