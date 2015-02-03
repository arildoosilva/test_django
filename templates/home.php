{% extends 'base.php' %}
{% block content %}
<div class="row-fluid">
{% for food in foods|slice:":3" %}
<div class="span4">
	<h2>{{ food.title }}</h2>
	<p>{{ food.description }}</p>
	<p><a class="btn" href="#">Detalhes &raquo;</a></p>
</div><!--/span-->
{% endfor %}
</div><!--/row-->
<div class="row-fluid">
{% for food in foods|slice:"3:" %}
<div class="span4">
	<h2>{{ food.title }}</h2>
	<p>{{ food.description }}</p>
	<p><a class="btn" href="#">Detalhes &raquo;</a></p>
</div><!--/span-->
{% endfor %}
</div><!--/row-->
{% endblock %}

