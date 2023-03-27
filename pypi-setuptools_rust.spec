#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: pyproject
#
Name     : pypi-setuptools_rust
Version  : 1.5.2
Release  : 27
URL      : https://files.pythonhosted.org/packages/99/db/e4ecb483ffa194d632ed44bda32cb740e564789fed7e56c2be8e2a0e2aa6/setuptools-rust-1.5.2.tar.gz
Source0  : https://files.pythonhosted.org/packages/99/db/e4ecb483ffa194d632ed44bda32cb740e564789fed7e56c2be8e2a0e2aa6/setuptools-rust-1.5.2.tar.gz
Summary  : Setuptools Rust extension plugin
Group    : Development/Tools
License  : MIT
Requires: pypi-setuptools_rust-license = %{version}-%{release}
Requires: pypi-setuptools_rust-python = %{version}-%{release}
Requires: pypi-setuptools_rust-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(setuptools)
BuildRequires : pypi(setuptools_rust)
BuildRequires : pypi(wheel)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
# Setuptools plugin for Rust extensions
[![github actions](https://github.com/PyO3/setuptools-rust/actions/workflows/ci.yml/badge.svg)](https://github.com/PyO3/setuptools-rust/actions/workflows/ci.yml)
[![pypi package](https://badge.fury.io/py/setuptools-rust.svg)](https://pypi.org/project/setuptools-rust/)
[![readthedocs](https://readthedocs.org/projects/pip/badge/)](https://setuptools-rust.readthedocs.io/en/latest/)
[![code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)

%package license
Summary: license components for the pypi-setuptools_rust package.
Group: Default

%description license
license components for the pypi-setuptools_rust package.


%package python
Summary: python components for the pypi-setuptools_rust package.
Group: Default
Requires: pypi-setuptools_rust-python3 = %{version}-%{release}

%description python
python components for the pypi-setuptools_rust package.


%package python3
Summary: python3 components for the pypi-setuptools_rust package.
Group: Default
Requires: python3-core
Provides: pypi(setuptools_rust)
Requires: pypi(semantic_version)
Requires: pypi(setuptools)
Requires: pypi(setuptools_rust)
Requires: pypi(typing_extensions)
Requires: pypi(wheel)

%description python3
python3 components for the pypi-setuptools_rust package.


%prep
%setup -q -n setuptools-rust-1.5.2
cd %{_builddir}/setuptools-rust-1.5.2
pushd ..
cp -a setuptools-rust-1.5.2 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1679938395
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export FCFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export FFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export CXXFLAGS="$CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export MAKEFLAGS=%{?_smp_mflags}
python3 -m build --wheel --skip-dependency-check --no-isolation
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -m build --wheel --skip-dependency-check --no-isolation

popd

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-setuptools_rust
cp %{_builddir}/setuptools-rust-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/pypi-setuptools_rust/b6d59af9754634678ceb503c91126c4248bf14c3 || :
pip install --root=%{buildroot} --no-deps --ignore-installed dist/*.whl
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
pip install --root=%{buildroot}-v3 --no-deps --ignore-installed dist/*.whl
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-setuptools_rust/b6d59af9754634678ceb503c91126c4248bf14c3

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
