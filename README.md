Aigapages
=========

Aigapages permite aprovechar la información bibliográfica que ofrece
[Aigaion](http://www.aigaion.nl/) para ser mostrada en las páginas personales
de un grupo de investigación.  Para ello, Aigapages funciona como un front-end
a la base de datos de Aigaion.

Requisitos
----------

* django
* perl
	* Tex::Encode

Instalación y configuración
---------------------------

 1. Descomprimir
 2. Compilar los locales (django-admin compilemessages)
 3. Configurar
 [settings.py](http://docs.djangoproject.com/en/1.2/topics/settings/). Prestar
 atención a las variables:
     - DEBUG establecer a False una vez todo funcione
     - ATTACHMENT\_DIR debe apuntar al directorio donde Aigaion guarda los
       adjuntos a los artículos
     - TEMPLATE\_DIRS debe contener la ruta absoluta al directorio bib/templates
     - DATABASE\_\* debe tener la misma conexión que Aigaion
 4. Establecer la lista de autores activos. Se debe editar _authors.py_ para
 indicar el identificador de autor y la URL de su página personal. En el caso
 del autor Javier López con id 448 y página personal http://someurl.com:
   > author_list = {
   >    448: 'http://someurl.com', # Javier Lopez
   > }
 5. Desplegar la aplicación siguiendo la [documentación oficial de
 Django](http://docs.djangoproject.com/en/1.2/howto/deployment/)
 6. Integrar las páginas de Aigapages con las páginas personales. Para esto se
 recomienda utilizar etiquetas object.

FAQ
---

 1. ¿Cómo muestro (o evito que se muestre) el enlace al texto completo?

    El enlace al texto completo se corresponde con el adjunto principal del
    artículo.

 2. ¿Cómo asocio una publicación a un proyecto?

    Añadiendo como userfield el campo project. Por ejemplo:

    > project={PROYECTO},

 3. ¿Cómo sé qué páginas se generan?

    Visitando la página raíz de Aigapages.

