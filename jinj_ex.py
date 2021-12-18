from jinja2 import Template
table=input("Enter table name:")
i=1
column='done'
while column!='done' or column!='DONE':
    column=input(f'Enter column {i+1}: ')
    column={}
    i+=1
print(column)
tm = Template("Select{% for i in range(10) %} {{i+1}}{%if not loop.last%},{% endif %}{% endfor %} from {{table}};")
msg = tm.render(table=table)
print(msg)