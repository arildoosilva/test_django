{% extends 'base.php' %}
{% block content %}
<form method='POST' action=''> {% csrf_token%}
	{{ form.as_p }}
	<input type='submit' value='Add' class='btn'/>
</form>
{% endblock %}