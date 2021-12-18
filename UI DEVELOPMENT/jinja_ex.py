from jinja2 import Template
tm = Template("Select{% for i in range(10) %} {{i+1}}{%if not loop.last%},{% endif %}{% endfor %} from emp")
msg = Template.render(tm)
n=input(msg)
print(n)