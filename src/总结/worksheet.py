"""
sheet.autofit(axis=None)如果参数省略，表示自动适应调整列宽和行高
若设置未"rows"或"r"，表示自动适应调整行高，若设置为"columns"或"c"
表示自动适应调整列宽
"""
"""
调整行高和列宽，可以使用column_width和row_height属性
value = sheet.range("A1").expand("table")  
value.column_width = X
value.row_height = Y 
"""
