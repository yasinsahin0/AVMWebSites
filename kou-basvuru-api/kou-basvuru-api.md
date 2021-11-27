# Kou Başvuru APİ

{% swagger method="get" path="" baseUrl="" summary="" %}
{% swagger-description %}

{% endswagger-description %}
{% endswagger %}

{% swagger method="post" path="" baseUrl="http://172.104.152.183:5000/DatabaseLogin" summary="Login" %}
{% swagger-description %}

{% endswagger-description %}

{% swagger-parameter in="query" name="TCNo" %}

{% endswagger-parameter %}

{% swagger-parameter in="query" name="Password" %}

{% endswagger-parameter %}

{% swagger-response status="200: OK" description="'admins' or 'users'" %}
```javascript
{
    // Response
}
```
{% endswagger-response %}

{% swagger-response status="400: Bad Request" description="False" %}
```javascript
{
    // Response
}
```
{% endswagger-response %}
{% endswagger %}

{% swagger method="post" path="" baseUrl="http://172.104.152.183:5000/DatabaseRegistry" summary="User Registry" %}
{% swagger-description %}

{% endswagger-description %}

{% swagger-parameter in="query" name="StudentNo" %}

{% endswagger-parameter %}

{% swagger-parameter in="query" name="TCNo" %}

{% endswagger-parameter %}

{% swagger-parameter in="query" name="Name" %}

{% endswagger-parameter %}

{% swagger-parameter in="query" name="Surname" %}

{% endswagger-parameter %}

{% swagger-parameter in="query" name="Email" %}

{% endswagger-parameter %}

{% swagger-parameter in="query" name="PhoneNo" %}

{% endswagger-parameter %}

{% swagger-parameter in="query" name="HomeAddress" %}

{% endswagger-parameter %}

{% swagger-parameter in="query" name="BusinessAddress" %}

{% endswagger-parameter %}

{% swagger-parameter in="query" name="DateOfBrith" %}

{% endswagger-parameter %}

{% swagger-parameter in="query" name="UniversityName" %}

{% endswagger-parameter %}

{% swagger-parameter in="query" name="DepartmanName" %}

{% endswagger-parameter %}

{% swagger-parameter in="query" name="SectionName" %}

{% endswagger-parameter %}

{% swagger-parameter in="query" name="Rate" %}

{% endswagger-parameter %}

{% swagger-parameter in="query" name="Password" %}

{% endswagger-parameter %}

{% swagger-parameter in="query" name="ProfilePhotoBase64" %}

{% endswagger-parameter %}

{% swagger-response status="200: OK" description="True" %}
```javascript
{
    // Response
}
```
{% endswagger-response %}

{% swagger-response status="400: Bad Request" description="False" %}
```javascript
{
    // Response
}
```
{% endswagger-response %}
{% endswagger %}
