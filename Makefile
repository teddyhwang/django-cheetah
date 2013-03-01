PROJECTNAME = {{ project_name }}

OUTPUT      = www/

DATE        = $(shell date +%I:%M%p)

CHECK       = \033[32m✔\033[39m

HR          =-------------------------------------------------------
DR          ========================================================


PLATFORM    = $(shell uname)


#
# BUILD
#

build:
	@echo
	@echo "\n${DR}"
	@echo "Buildig Project ${PROJECTNAME}..."
	@echo "${HR}\n"
	@rm -rf ${OUTPUT}*
	@echo "\n Cleaning out build folder...                    ${CHECK} Done"
	@sed -i '' "s/DEBUG\ =\ True/DEBUG\ =\ False/" ecommerce/settings.py
	@echo "\n Setting DEBUG to False in Django...             ${CHECK} Done \n"
	@python manage.py staticsitegen
	@echo "\n Exporting static HTML files...                  ${CHECK} Done \n"
	@python manage.py collectstatic --noinput
	@echo "\n Compiling media assets...                       ${CHECK} Done"
	@uglifyjs ${OUTPUT}media/lib/modernizr/modernizr.js > ${OUTPUT}media/compiled/js/modernizr.min.js
	@echo "\n Compiling modernizr...                          ${CHECK} Done"
	@rm -rf ${OUTPUT}media/css/*.less
	@echo "\n Removing all LESS files from build...           ${CHECK} Done"
	@sed -i '' "s/\=\"\//\=\"/g" ${OUTPUT}*.html
	@sed -i '' "s/href\=\"\"/href\=\"index\.html\"/g" ${OUTPUT}*.html
	@echo "\n Creating relative links in HTML build...        ${CHECK} Done"
	@sed -i '' "s/DEBUG\ =\ False/DEBUG\ =\ True/" ecommerce/settings.py
	@echo "\n Setting DEBUG back to True in Django...         ${CHECK} Done \n"
	@echo "\n${HR}"
	@echo "${PROJECTNAME} built and compiled successfully at ${DATE}."
	@echo "${DR}\n"

addmediator:
ifndef page
	$(error missing variable "page")
else
	@echo
	@echo "\n${DR}"
	@echo "Adding \"${page}\" as a new mediator for requirejs..."
	@echo "${HR}\n"
	@cp media/js/build/homepage.js media/js/build/${page}.js
	@cp media/js/config/homepage.js media/js/config/${page}.js
	@cp media/js/mediators/example.js media/js/mediators/${page}.js
	@echo "\n Copying mediator from homepage...               ${CHECK} Done"
	@sed -i '' "s/homepage/${page}/g" media/js/build/${page}.js
	@sed -i '' "s/homepage/${page}/g" media/js/config/${page}.js
	@echo "\n Adding proper references...                     ${CHECK} Done"
	@echo "\n${HR}"
	@echo "${page} successfully added at ${DATE}. \n\nBe sure to add the \"${page}\" reference into \nREQUIRE_STANDALONE_MODULES in settings.py"
	@echo "${DR}\n"
endif
