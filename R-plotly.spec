#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-plotly
Version  : 4.7.1
Release  : 2
URL      : https://cran.r-project.org/src/contrib/plotly_4.7.1.tar.gz
Source0  : https://cran.r-project.org/src/contrib/plotly_4.7.1.tar.gz
Summary  : Create Interactive Web Graphics via 'plotly.js'
Group    : Development/Tools
License  : MIT
Requires: R-base64enc
Requires: R-crosstalk
Requires: R-data.table
Requires: R-dplyr
Requires: R-ggplot2
Requires: R-hexbin
Requires: R-htmlwidgets
Requires: R-httr
Requires: R-purrr
Requires: R-tidyr
BuildRequires : R-base64enc
BuildRequires : R-crosstalk
BuildRequires : R-data.table
BuildRequires : R-dplyr
BuildRequires : R-ggplot2
BuildRequires : R-hexbin
BuildRequires : R-htmlwidgets
BuildRequires : R-httr
BuildRequires : R-purrr
BuildRequires : R-tidyr
BuildRequires : clr-R-helpers

%description
[![Build Status](https://travis-ci.org/ropensci/plotly.png?branch=master)](https://travis-ci.org/ropensci/plotly)

%prep
%setup -q -c -n plotly

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1521270720

%install
rm -rf %{buildroot}
export SOURCE_DATE_EPOCH=1521270720
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
/usr/lib64/R/library/plotly/demo/crosstalk-highlight-binned-target.R
/usr/lib64/R/library/plotly/demo/crosstalk-highlight-epl.R
/usr/lib64/R/library/plotly/demo/crosstalk-highlight-ggpairs.R
/usr/lib64/R/library/plotly/demo/crosstalk-highlight-ggplotly.R
/usr/lib64/R/library/plotly/demo/crosstalk-highlight-intro.R
/usr/lib64/R/library/plotly/demo/crosstalk-highlight-leaflet.R
/usr/lib64/R/library/plotly/demo/crosstalk-highlight-pipeline.R
/usr/lib64/R/library/plotly/demo/crosstalk-highlight-subplot.R
/usr/lib64/R/library/plotly/demo/rotate.R
/usr/lib64/R/library/plotly/demo/ternary.R
/usr/lib64/R/library/plotly/docs.R
/usr/lib64/R/library/plotly/examples/rmd/flexdashboard/index.Rmd
/usr/lib64/R/library/plotly/examples/rmd/onRenderHover/index.Rmd
/usr/lib64/R/library/plotly/examples/rmd/printing/index.Rmd
/usr/lib64/R/library/plotly/examples/shiny/DT/app.R
/usr/lib64/R/library/plotly/examples/shiny/Diamonds/server.R
/usr/lib64/R/library/plotly/examples/shiny/Diamonds/ui.R
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
/usr/lib64/R/library/plotly/examples/shiny/basic/DESCRIPTION
/usr/lib64/R/library/plotly/examples/shiny/basic/app.R
/usr/lib64/R/library/plotly/examples/shiny/event_data/DESCRIPTION
/usr/lib64/R/library/plotly/examples/shiny/event_data/app.R
/usr/lib64/R/library/plotly/examples/shiny/event_data_3D/app.R
/usr/lib64/R/library/plotly/examples/shiny/event_data_click/DESCRIPTION
/usr/lib64/R/library/plotly/examples/shiny/event_data_click/app.R
/usr/lib64/R/library/plotly/examples/shiny/event_data_click_map/app.R
/usr/lib64/R/library/plotly/examples/shiny/event_data_modules/app.R
/usr/lib64/R/library/plotly/examples/shiny/event_data_select/app.R
/usr/lib64/R/library/plotly/examples/shiny/lmGadget/app.R
/usr/lib64/R/library/plotly/examples/shiny/proxy_mapbox/app.R
/usr/lib64/R/library/plotly/examples/shiny/proxy_relayout/app.R
/usr/lib64/R/library/plotly/examples/shiny/proxy_restyle_canada/app.R
/usr/lib64/R/library/plotly/examples/shiny/proxy_restyle_economics/app.R
/usr/lib64/R/library/plotly/help/AnIndex
/usr/lib64/R/library/plotly/help/aliases.rds
/usr/lib64/R/library/plotly/help/paths.rds
/usr/lib64/R/library/plotly/help/plotly.rdb
/usr/lib64/R/library/plotly/help/plotly.rdx
/usr/lib64/R/library/plotly/html/00Index.html
/usr/lib64/R/library/plotly/html/R.css
/usr/lib64/R/library/plotly/htmlwidgets/lib/colourpicker/LICENSE
/usr/lib64/R/library/plotly/htmlwidgets/lib/colourpicker/colourpicker.min.css
/usr/lib64/R/library/plotly/htmlwidgets/lib/colourpicker/colourpicker.min.js
/usr/lib64/R/library/plotly/htmlwidgets/lib/plotlyjs/LICENSE
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
