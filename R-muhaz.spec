#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-muhaz
Version  : 1.2.6.1
Release  : 7
URL      : https://cran.r-project.org/src/contrib/muhaz_1.2.6.1.tar.gz
Source0  : https://cran.r-project.org/src/contrib/muhaz_1.2.6.1.tar.gz
Summary  : Hazard Function Estimation in Survival Analysis
Group    : Development/Tools
License  : GPL-2.0
Requires: R-muhaz-lib = %{version}-%{release}
BuildRequires : buildreq-R

%description
This software may be distributed under the terms of the General Public License.
See the file COPYING to determine your rights.

%package lib
Summary: lib components for the R-muhaz package.
Group: Libraries

%description lib
lib components for the R-muhaz package.


%prep
%setup -q -c -n muhaz

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1548542195

%install
export SOURCE_DATE_EPOCH=1548542195
rm -rf %{buildroot}
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
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library muhaz
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library muhaz
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library muhaz
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc -l %{buildroot}/usr/lib64/R/library muhaz|| : 
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/muhaz/DESCRIPTION
/usr/lib64/R/library/muhaz/INDEX
/usr/lib64/R/library/muhaz/Meta/Rd.rds
/usr/lib64/R/library/muhaz/Meta/features.rds
/usr/lib64/R/library/muhaz/Meta/hsearch.rds
/usr/lib64/R/library/muhaz/Meta/links.rds
/usr/lib64/R/library/muhaz/Meta/nsInfo.rds
/usr/lib64/R/library/muhaz/Meta/package.rds
/usr/lib64/R/library/muhaz/NAMESPACE
/usr/lib64/R/library/muhaz/R/muhaz
/usr/lib64/R/library/muhaz/R/muhaz.rdb
/usr/lib64/R/library/muhaz/R/muhaz.rdx
/usr/lib64/R/library/muhaz/help/AnIndex
/usr/lib64/R/library/muhaz/help/aliases.rds
/usr/lib64/R/library/muhaz/help/muhaz.rdb
/usr/lib64/R/library/muhaz/help/muhaz.rdx
/usr/lib64/R/library/muhaz/help/paths.rds
/usr/lib64/R/library/muhaz/html/00Index.html
/usr/lib64/R/library/muhaz/html/R.css
/usr/lib64/R/library/muhaz/libs/symbols.rds

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/muhaz/libs/muhaz.so
/usr/lib64/R/library/muhaz/libs/muhaz.so.avx2
/usr/lib64/R/library/muhaz/libs/muhaz.so.avx512
