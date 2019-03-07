#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-plotly
Version  : 4.8.0
Release  : 16
URL      : https://cran.r-project.org/src/contrib/plotly_4.8.0.tar.gz
Source0  : https://cran.r-project.org/src/contrib/plotly_4.8.0.tar.gz
Summary  : Create Interactive Web Graphics via 'plotly.js'
Group    : Development/Tools
License  : MIT
Requires: R-RColorBrewer
Requires: R-assertthat
BuildRequires : R-RColorBrewer
BuildRequires : R-assertthat
BuildRequires : R-base64enc
BuildRequires : R-crosstalk
BuildRequires : R-data.table
BuildRequires : R-dplyr
BuildRequires : R-ggplot2
BuildRequires : R-hexbin
BuildRequires : R-htmlwidgets
BuildRequires : R-httr
BuildRequires : R-listviewer
BuildRequires : R-promises
BuildRequires : R-tidyr
BuildRequires : buildreq-R

%description
<img src="man/figures/plotly.png" width="200" />
[![Build
Status](https://travis-ci.org/ropensci/plotly.png?branch=master)](https://travis-ci.org/ropensci/plotly)
[![CRAN
Status](http://www.r-pkg.org/badges/version/plotly)](http://cran.r-project.org/package=plotly)
[![CRAN
Downloads](http://cranlogs.r-pkg.org/badges/grand-total/plotly)](https://www.rpackages.io/package/plotly)
[![monthly](https://cranlogs.r-pkg.org/badges/plotly)](https://www.rpackages.io/package/plotly)

%prep
%setup -q -c -n plotly

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1538581706

%install
rm -rf %{buildroot}
export SOURCE_DATE_EPOCH=1538581706
export LANG=C
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library plotly
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library plotly
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library plotly
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc -l %{buildroot}/usr/lib64/R/library plotly|| : 
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/plotly/CITATION
/usr/lib64/R/library/plotly/DESCRIPTION
/usr/lib64/R/library/plotly/INDEX
/usr/lib64/R/library/plotly/LICENSE
/usr/lib64/R/library/plotly/Meta/Rd.rds
/usr/lib64/R/library/plotly/Meta/data.rds
/usr/lib64/R/library/plotly/Meta/demo.rds
/usr/lib64/R/library/plotly/Meta/features.rds
/usr/lib64/R/library/plotly/Meta/hsearch.rds
/usr/lib64/R/library/plotly/Meta/links.rds
/usr/lib64/R/library/plotly/Meta/nsInfo.rds
/usr/lib64/R/library/plotly/Meta/package.rds
/usr/lib64/R/library/plotly/NAMESPACE
/usr/lib64/R/library/plotly/NEWS.md
/usr/lib64/R/library/plotly/R/plotly
/usr/lib64/R/library/plotly/R/plotly.rdb
/usr/lib64/R/library/plotly/R/plotly.rdx
/usr/lib64/R/library/plotly/R/sysdata.rdb
/usr/lib64/R/library/plotly/R/sysdata.rdx
/usr/lib64/R/library/plotly/build-push-comment.R
/usr/lib64/R/library/plotly/data/Rdata.rdb
/usr/lib64/R/library/plotly/data/Rdata.rds
/usr/lib64/R/library/plotly/data/Rdata.rdx
/usr/lib64/R/library/plotly/demo/animation-tour-USArrests.R
/usr/lib64/R/library/plotly/demo/animation-tour-basic.R
/usr/lib64/R/library/plotly/demo/crosstalk-filter-dynamic-axis.R
/usr/lib64/R/library/plotly/demo/crosstalk-filter-lines.R
/usr/lib64/R/library/plotly/demo/crosstalk-highlight-binned-target-a.R
/usr/lib64/R/library/plotly/demo/crosstalk-highlight-binned-target-b.R
/usr/lib64/R/library/plotly/demo/crosstalk-highlight-binned-target-c.R
/usr/lib64/R/library/plotly/demo/crosstalk-highlight-epl-2.R
/usr/lib64/R/library/plotly/demo/crosstalk-highlight-epl.R
/usr/lib64/R/library/plotly/demo/crosstalk-highlight-ggpairs.R
/usr/lib64/R/library/plotly/demo/crosstalk-highlight-ggplotly.R
/usr/lib64/R/library/plotly/demo/crosstalk-highlight-intro.R
/usr/lib64/R/library/plotly/demo/crosstalk-highlight-leaflet.R
/usr/lib64/R/library/plotly/demo/crosstalk-highlight-pipeline.R
/usr/lib64/R/library/plotly/demo/crosstalk-highlight-subplot.R
/usr/lib64/R/library/plotly/demo/custom-javascript.R
/usr/lib64/R/library/plotly/demo/rotate.R
/usr/lib64/R/library/plotly/demo/sf-dt.R
/usr/lib64/R/library/plotly/demo/sf-geo.R
/usr/lib64/R/library/plotly/demo/sf-ggplot2.R
/usr/lib64/R/library/plotly/demo/sf-mapbox-data.R
/usr/lib64/R/library/plotly/demo/sf-mapbox-layout.R
/usr/lib64/R/library/plotly/demo/sf-mapbox-style.R
/usr/lib64/R/library/plotly/demo/sf-plotly-3D-globe.R
/usr/lib64/R/library/plotly/demo/sf-plotly-storms.R
/usr/lib64/R/library/plotly/demo/ternary.R
/usr/lib64/R/library/plotly/docs.R
/usr/lib64/R/library/plotly/examples/rmd/MathJax/index.Rmd
/usr/lib64/R/library/plotly/examples/rmd/flexdashboard/index.Rmd
/usr/lib64/R/library/plotly/examples/rmd/onRenderHover/index.Rmd
/usr/lib64/R/library/plotly/examples/rmd/printing/index.Rmd
/usr/lib64/R/library/plotly/examples/shiny/DT/app.R
/usr/lib64/R/library/plotly/examples/shiny/Diamonds/server.R
/usr/lib64/R/library/plotly/examples/shiny/Diamonds/ui.R
/usr/lib64/R/library/plotly/examples/shiny/MathJax/app.R
/usr/lib64/R/library/plotly/examples/shiny/Movies/server.R
/usr/lib64/R/library/plotly/examples/shiny/Movies/ui.R
/usr/lib64/R/library/plotly/examples/shiny/UN_Advanced/Data/UN_IdealPoints.csv
/usr/lib64/R/library/plotly/examples/shiny/UN_Advanced/global.R
/usr/lib64/R/library/plotly/examples/shiny/UN_Advanced/server.R
/usr/lib64/R/library/plotly/examples/shiny/UN_Advanced/ui.R
/usr/lib64/R/library/plotly/examples/shiny/UN_Simple/Data/UN_IdealPoints.csv
/usr/lib64/R/library/plotly/examples/shiny/UN_Simple/global.R
/usr/lib64/R/library/plotly/examples/shiny/UN_Simple/server.R
/usr/lib64/R/library/plotly/examples/shiny/UN_Simple/ui.R
/usr/lib64/R/library/plotly/examples/shiny/async/app.R
/usr/lib64/R/library/plotly/examples/shiny/basic/DESCRIPTION
/usr/lib64/R/library/plotly/examples/shiny/basic/app.R
/usr/lib64/R/library/plotly/examples/shiny/event_data/DESCRIPTION
/usr/lib64/R/library/plotly/examples/shiny/event_data/app.R
/usr/lib64/R/library/plotly/examples/shiny/event_data_3D/app.R
/usr/lib64/R/library/plotly/examples/shiny/event_data_click/DESCRIPTION
/usr/lib64/R/library/plotly/examples/shiny/event_data_click/app.R
/usr/lib64/R/library/plotly/examples/shiny/event_data_click_map/app.R
/usr/lib64/R/library/plotly/examples/shiny/event_data_modules/app.R
/usr/lib64/R/library/plotly/examples/shiny/event_data_persist/app.R
/usr/lib64/R/library/plotly/examples/shiny/event_data_select/app.R
/usr/lib64/R/library/plotly/examples/shiny/ggplotly_sizing/app.R
/usr/lib64/R/library/plotly/examples/shiny/lmGadget/app.R
/usr/lib64/R/library/plotly/examples/shiny/proxy_mapbox/app.R
/usr/lib64/R/library/plotly/examples/shiny/proxy_relayout/app.R
/usr/lib64/R/library/plotly/examples/shiny/proxy_restyle_canada/app.R
/usr/lib64/R/library/plotly/examples/shiny/proxy_restyle_economics/app.R
/usr/lib64/R/library/plotly/help/AnIndex
/usr/lib64/R/library/plotly/help/aliases.rds
/usr/lib64/R/library/plotly/help/figures/plotly.png
/usr/lib64/R/library/plotly/help/figures/plotly.svg
/usr/lib64/R/library/plotly/help/paths.rds
/usr/lib64/R/library/plotly/help/plotly.rdb
/usr/lib64/R/library/plotly/help/plotly.rdx
/usr/lib64/R/library/plotly/html/00Index.html
/usr/lib64/R/library/plotly/html/R.css
/usr/lib64/R/library/plotly/htmlwidgets/lib/colourpicker/LICENSE
/usr/lib64/R/library/plotly/htmlwidgets/lib/colourpicker/colourpicker.min.css
/usr/lib64/R/library/plotly/htmlwidgets/lib/colourpicker/colourpicker.min.js
/usr/lib64/R/library/plotly/htmlwidgets/lib/mathjax/cdn.js
/usr/lib64/R/library/plotly/htmlwidgets/lib/plotlyjs/LICENSE
/usr/lib64/R/library/plotly/htmlwidgets/lib/plotlyjs/locales/af.js
/usr/lib64/R/library/plotly/htmlwidgets/lib/plotlyjs/locales/am.js
/usr/lib64/R/library/plotly/htmlwidgets/lib/plotlyjs/locales/ar-dz.js
/usr/lib64/R/library/plotly/htmlwidgets/lib/plotlyjs/locales/ar-eg.js
/usr/lib64/R/library/plotly/htmlwidgets/lib/plotlyjs/locales/ar.js
/usr/lib64/R/library/plotly/htmlwidgets/lib/plotlyjs/locales/az.js
/usr/lib64/R/library/plotly/htmlwidgets/lib/plotlyjs/locales/bg.js
/usr/lib64/R/library/plotly/htmlwidgets/lib/plotlyjs/locales/bs.js
/usr/lib64/R/library/plotly/htmlwidgets/lib/plotlyjs/locales/ca.js
/usr/lib64/R/library/plotly/htmlwidgets/lib/plotlyjs/locales/cs.js
/usr/lib64/R/library/plotly/htmlwidgets/lib/plotlyjs/locales/da.js
/usr/lib64/R/library/plotly/htmlwidgets/lib/plotlyjs/locales/de-ch.js
/usr/lib64/R/library/plotly/htmlwidgets/lib/plotlyjs/locales/de.js
/usr/lib64/R/library/plotly/htmlwidgets/lib/plotlyjs/locales/el.js
/usr/lib64/R/library/plotly/htmlwidgets/lib/plotlyjs/locales/eo.js
/usr/lib64/R/library/plotly/htmlwidgets/lib/plotlyjs/locales/es-ar.js
/usr/lib64/R/library/plotly/htmlwidgets/lib/plotlyjs/locales/es-pe.js
/usr/lib64/R/library/plotly/htmlwidgets/lib/plotlyjs/locales/es.js
/usr/lib64/R/library/plotly/htmlwidgets/lib/plotlyjs/locales/et.js
/usr/lib64/R/library/plotly/htmlwidgets/lib/plotlyjs/locales/eu.js
/usr/lib64/R/library/plotly/htmlwidgets/lib/plotlyjs/locales/fa.js
/usr/lib64/R/library/plotly/htmlwidgets/lib/plotlyjs/locales/fi.js
/usr/lib64/R/library/plotly/htmlwidgets/lib/plotlyjs/locales/fo.js
/usr/lib64/R/library/plotly/htmlwidgets/lib/plotlyjs/locales/fr-ch.js
/usr/lib64/R/library/plotly/htmlwidgets/lib/plotlyjs/locales/fr.js
/usr/lib64/R/library/plotly/htmlwidgets/lib/plotlyjs/locales/gl.js
/usr/lib64/R/library/plotly/htmlwidgets/lib/plotlyjs/locales/gu.js
/usr/lib64/R/library/plotly/htmlwidgets/lib/plotlyjs/locales/he.js
/usr/lib64/R/library/plotly/htmlwidgets/lib/plotlyjs/locales/hi-in.js
/usr/lib64/R/library/plotly/htmlwidgets/lib/plotlyjs/locales/hr.js
/usr/lib64/R/library/plotly/htmlwidgets/lib/plotlyjs/locales/hu.js
/usr/lib64/R/library/plotly/htmlwidgets/lib/plotlyjs/locales/hy.js
/usr/lib64/R/library/plotly/htmlwidgets/lib/plotlyjs/locales/id.js
/usr/lib64/R/library/plotly/htmlwidgets/lib/plotlyjs/locales/is.js
/usr/lib64/R/library/plotly/htmlwidgets/lib/plotlyjs/locales/it.js
/usr/lib64/R/library/plotly/htmlwidgets/lib/plotlyjs/locales/ja.js
/usr/lib64/R/library/plotly/htmlwidgets/lib/plotlyjs/locales/ka.js
/usr/lib64/R/library/plotly/htmlwidgets/lib/plotlyjs/locales/km.js
/usr/lib64/R/library/plotly/htmlwidgets/lib/plotlyjs/locales/ko.js
/usr/lib64/R/library/plotly/htmlwidgets/lib/plotlyjs/locales/lt.js
/usr/lib64/R/library/plotly/htmlwidgets/lib/plotlyjs/locales/lv.js
/usr/lib64/R/library/plotly/htmlwidgets/lib/plotlyjs/locales/me-me.js
/usr/lib64/R/library/plotly/htmlwidgets/lib/plotlyjs/locales/me.js
/usr/lib64/R/library/plotly/htmlwidgets/lib/plotlyjs/locales/mk.js
/usr/lib64/R/library/plotly/htmlwidgets/lib/plotlyjs/locales/ml.js
/usr/lib64/R/library/plotly/htmlwidgets/lib/plotlyjs/locales/ms.js
/usr/lib64/R/library/plotly/htmlwidgets/lib/plotlyjs/locales/mt.js
/usr/lib64/R/library/plotly/htmlwidgets/lib/plotlyjs/locales/nl-be.js
/usr/lib64/R/library/plotly/htmlwidgets/lib/plotlyjs/locales/nl.js
/usr/lib64/R/library/plotly/htmlwidgets/lib/plotlyjs/locales/no.js
/usr/lib64/R/library/plotly/htmlwidgets/lib/plotlyjs/locales/pa.js
/usr/lib64/R/library/plotly/htmlwidgets/lib/plotlyjs/locales/pl.js
/usr/lib64/R/library/plotly/htmlwidgets/lib/plotlyjs/locales/pt-br.js
/usr/lib64/R/library/plotly/htmlwidgets/lib/plotlyjs/locales/rm.js
/usr/lib64/R/library/plotly/htmlwidgets/lib/plotlyjs/locales/ro.js
/usr/lib64/R/library/plotly/htmlwidgets/lib/plotlyjs/locales/ru.js
/usr/lib64/R/library/plotly/htmlwidgets/lib/plotlyjs/locales/sk.js
/usr/lib64/R/library/plotly/htmlwidgets/lib/plotlyjs/locales/sl.js
/usr/lib64/R/library/plotly/htmlwidgets/lib/plotlyjs/locales/sq.js
/usr/lib64/R/library/plotly/htmlwidgets/lib/plotlyjs/locales/sr-sr.js
/usr/lib64/R/library/plotly/htmlwidgets/lib/plotlyjs/locales/sr.js
/usr/lib64/R/library/plotly/htmlwidgets/lib/plotlyjs/locales/sv.js
/usr/lib64/R/library/plotly/htmlwidgets/lib/plotlyjs/locales/sw.js
/usr/lib64/R/library/plotly/htmlwidgets/lib/plotlyjs/locales/ta.js
/usr/lib64/R/library/plotly/htmlwidgets/lib/plotlyjs/locales/th.js
/usr/lib64/R/library/plotly/htmlwidgets/lib/plotlyjs/locales/tr.js
/usr/lib64/R/library/plotly/htmlwidgets/lib/plotlyjs/locales/tt.js
/usr/lib64/R/library/plotly/htmlwidgets/lib/plotlyjs/locales/uk.js
/usr/lib64/R/library/plotly/htmlwidgets/lib/plotlyjs/locales/ur.js
/usr/lib64/R/library/plotly/htmlwidgets/lib/plotlyjs/locales/vi.js
/usr/lib64/R/library/plotly/htmlwidgets/lib/plotlyjs/locales/zh-cn.js
/usr/lib64/R/library/plotly/htmlwidgets/lib/plotlyjs/locales/zh-hk.js
/usr/lib64/R/library/plotly/htmlwidgets/lib/plotlyjs/locales/zh-tw.js
/usr/lib64/R/library/plotly/htmlwidgets/lib/plotlyjs/plotly-htmlwidgets.css
/usr/lib64/R/library/plotly/htmlwidgets/lib/plotlyjs/plotly-latest.min.js
/usr/lib64/R/library/plotly/htmlwidgets/lib/selectize/selectize.bootstrap3.css
/usr/lib64/R/library/plotly/htmlwidgets/lib/selectize/selectize.min.js
/usr/lib64/R/library/plotly/htmlwidgets/lib/typedarray/LICENSE
/usr/lib64/R/library/plotly/htmlwidgets/lib/typedarray/typedarray.min.js
/usr/lib64/R/library/plotly/htmlwidgets/plotly.js
/usr/lib64/R/library/plotly/htmlwidgets/plotly.yaml
/usr/lib64/R/library/plotly/plotlyjs.R
/usr/lib64/R/library/plotly/stars.R
