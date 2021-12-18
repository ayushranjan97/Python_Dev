from jinja2 import Template
table=input("Enter table name:")
tm = Template("Select{% for i in range(10) %} {{i+1}}{%if not loop.last%},{% endif %}{% endfor %} from {{table}};")
msg = tm.render(table=table)
print(msg)