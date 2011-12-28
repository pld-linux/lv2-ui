Summary:	LV2 UI extension - generic UI interface for LV2 plugins
Summary(pl.UTF-8):	Rozszerzenie LV2 UI - ogólny interfejs do interfejsów użytkownika do wtyczek LV2
Name:		lv2-ui
Version:	2.4
Release:	1
License:	ISC
Group:		Libraries
Source0:	http://lv2plug.in/spec/%{name}-%{version}.tar.bz2
# Source0-md5:	42a9f6c79412babb7212ab60395114da
URL:		http://lv2plug.in/ns/extensions/ui/
BuildRequires:	python >= 1:2.6
BuildRequires:	python-modules >= 1:2.6
Requires:	lv2core >= 6.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
LV2 UI extension defines an interface that can be used in LV2 plugins
and hosts to create UIs for plugins. The UIs are similar to plugins
and reside in shared object files in an LV2 bundle.

%description -l pl.UTF-8
Rozszerzenie LV2 UI definiuje interfejs, który może być używany we
wtyczkach oraz hostach LV2 do tworzenia interfejsów użytkownika (UI)
do wtyczek. UI są podobne do wtyczek, są przechowywane w plikach
obiektów współdzielonych w pakietach LV2.

%package devel
Summary:	Header file for LV2 UI extension
Summary(pl.UTF-8):	Plik nagłówkowy rozszerzenia LV2 UI
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	lv2core-devel >= 6.0

%description devel
Header file for LV2 UI extension.

%description devel -l pl.UTF-8
Plik nagłówkowy rozszerzenia LV2 UI.

%prep
%setup -q

%build
./waf configure \
	--prefix=%{_prefix} \
	--libdir=%{_libdir}

./waf

%install
rm -rf $RPM_BUILD_ROOT

./waf install \
	--destdir=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc NEWS
%dir %{_libdir}/lv2/ui.lv2
%{_libdir}/lv2/ui.lv2/lv2-ui.doap.ttl
%{_libdir}/lv2/ui.lv2/ui.ttl
%{_libdir}/lv2/ui.lv2/manifest.ttl

%files devel
%defattr(644,root,root,755)
%{_libdir}/lv2/ui.lv2/ui.h
%{_includedir}/lv2/lv2plug.in/ns/extensions/ui
%{_pkgconfigdir}/lv2-lv2plug.in-ns-extensions-ui.pc
