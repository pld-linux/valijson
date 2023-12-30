Summary:	Header-only JSON Schema validation library for C++ 11
Summary(pl.UTF-8):	Biblioteka z samych nagłówków do sprawdzania poprawności względem JSON Schema dla C++ 11
Name:		valijson
Version:	1.0.2
Release:	1
License:	BSD
Group:		Development/Libraries
#Source0Download: https://github.com/tristanpenman/valijson/releases
Source0:	https://github.com/tristanpenman/valijson/archive/v%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	b9e698e90c372dc17d7b8a1cd77d4de8
URL:		https://github.com/tristanpenman/valijson
BuildRequires:	cmake >= 3.1.2
BuildRequires:	libstdc++-devel >= 6:4.7
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# nothing binary; not noarch because of cmake module path
%define		_enable_debug_packages	0

%description
Valijson is a header-only JSON Schema (<http://json-schema.org/>)
validation library for C++11.

Valijson provides a simple validation API that allows you to load JSON
Schemas, and validate documents loaded by one of several supported
parser libraries:
- boost::property_tree
- Boost.JSON
- json11
- jsoncpp
- nlohmann/json
- rapidjson
- PicoJSON
- Poco JSON
- Qt 5

%description -l pl.UTF-8
Valijson to biblioteka z samych nagłówków do sprawdzania poprawności
względem JSON Schema (<http://json-schema.org/>) dla C++ 11.

Valijson udostępnia proste API do sprawdzania poprawności, pozwalające
załadować schematy JSON Schema i sprawdzać dokumenty załadowane przy
użyciu jednej z kilku obsługiwanych bibliotek parserów:
- boost::property_tree
- Boost.JSON
- json11
- jsoncpp
- nlohmann/json
- rapidjson
- PicoJSON
- Poco JSON
- Qt 5

%package devel
Summary:	Header-only JSON Schema validation library for C++ 11
Summary(pl.UTF-8):	Biblioteka z samych nagłówków do sprawdzania poprawności JSON Schema dla C++ 11
Group:		Development/Libraries
Requires:	libstdc++-devel >= 6:4.7

%description devel
Valijson is a header-only JSON Schema (<http://json-schema.org/>)
validation library for C++11.

Valijson provides a simple validation API that allows you to load JSON
Schemas, and validate documents loaded by one of several supported
parser libraries:
- boost::property_tree
- Boost.JSON
- json11
- jsoncpp
- nlohmann/json
- rapidjson
- PicoJSON
- Poco JSON
- Qt 5

%description devel -l pl.UTF-8
Valijson to biblioteka z samych nagłówków do sprawdzania poprawności
względem JSON Schema (<http://json-schema.org/>) dla C++ 11.

Valijson udostępnia proste API do sprawdzania poprawności, pozwalające
załadować schematy JSON Schema i sprawdzać dokumenty załadowane przy
użyciu jednej z kilku obsługiwanych bibliotek parserów:
- boost::property_tree
- Boost.JSON
- json11
- jsoncpp
- nlohmann/json
- rapidjson
- PicoJSON
- Poco JSON
- Qt 5

%prep
%setup -q

%build
install -d build
cd build
%cmake .. \
	-Dvalijson_BUILD_EXAMPLES=OFF \
	-Dvalijson_BUILD_TESTS=OFF

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -p examples/*.cpp $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
%{__rm} $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}/valijson_nlohmann_bundled_test.cpp

%clean
rm -rf $RPM_BUILD_ROOT

%files devel
%defattr(644,root,root,755)
%doc Authors LICENSE README.md doc/*
%dir %{_includedir}/compat
%{_includedir}/compat/optional.hpp
%{_includedir}/valijson
%{_libdir}/cmake/valijson
%{_examplesdir}/%{name}-%{version}
