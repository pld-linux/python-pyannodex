Summary:	Python bindings for Annodex libraries
Summary(pl.UTF-8):	Wiązania Pythona dla bibliotek Annodex
Name:		python-pyannodex
Version:	0.7.3.2
Release:	1
License:	GPL v2+
Group:		Libraries/Python
Source0:	http://benno.id.au/code/pyannodex/pyannodex-%{version}.tar.gz
# Source0-md5:	2dea5d9527de147d6b8a09037798c6ad
URL:		http://benno.id.au/code/pyannodex/
BuildRequires:	libannodex-devel
BuildRequires:	python-devel >= 1:2.5
BuildRequires:	python-modules >= 1:2.5
BuildRequires:	rpm-pythonprov
%pyrequires_eq	python-libs
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Python bindings for Annodex libraries.

%description -l pl.UTF-8
Wiązania Pythona dla bibliotek Annodex.

%prep
%setup -q -n pyannodex-%{version}

%build
%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT
#install -d $RPM_BUILD_ROOT{%{py_sitedir},%{_examplesdir}/%{name}-%{version}}
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__python} setup.py install \
	--root=$RPM_BUILD_ROOT \
	--optimize=2

cp -a examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
# install as examples (just python reimplementation of C utils from libannodex)
mv $RPM_BUILD_ROOT%{_bindir}/anx*.py $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS NEWS README
%dir %{py_sitedir}/annodex
%attr(755,root,root) %{py_sitedir}/annodex/_annodex.so
%{py_sitedir}/annodex/*.py[co]
%{py_sitedir}/pyannodex-*.egg-info
%{_examplesdir}/%{name}-%{version}
