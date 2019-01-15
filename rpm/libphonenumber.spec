Name:          libphonenumber
# Newer release require com.google.protobuf.nano available only on protobuf >= 3.0.0-alpha-1
Version:       7.7.5
Release:       1%{?dist}
Summary:       Library to handle international phone numbers
# BSD:  cpp/src/phonenumbers/base/*
# tools/cpp/src/base/*
# MIT: cpp/src/phonenumbers/utf/rune.c
# cpp/src/phonenumbers/utf/utf.h
# cpp/src/phonenumbers/utf/utfdef.h
License:       ASL 2.0 and BSD and MIT
URL:           https://github.com/googlei18n/libphonenumber/
Source0:       https://github.com/googlei18n/libphonenumber/archive/%{name}-%{version}.tar.gz
# Use ${LIB_INSTALL_DIR} instead of hardcoded lib in cmake file

BuildRequires: boost-devel
BuildRequires: cmake
BuildRequires: gtest-devel
BuildRequires: pkgconfig(icu-uc)
BuildRequires: protobuf-compiler
BuildRequires: protobuf-devel
# BuildRequires: re2-devel


%description
Google's common C++ library for parsing, formatting,
storing and validating international phone numbers.
Optimized for running on  smart-phones.

This library is a C++ port of the Java version.

%package devel
Summary:  Development files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: protobuf-devel

%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%setup -q -n %{name}-%{version}

%build
mkdir build
cd build

cmake ../cpp \
    -DBUILD_GEOCODER=OFF \
    -DCMAKE_INSTALL_PREFIX=%{_prefix}

make %{?_smp_mflags}

%install
cd build

make install DESTDIR=%{buildroot}
find %{buildroot} -name '*.a' -delete
find %{buildroot} -name '*.la' -delete

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
# {_libdir}/libgeocoding.so.*
%{_libdir}/libphonenumber.so.*
%doc cpp/LICENSE
%doc cpp/README

%files devel
%dir %{_includedir}/phonenumbers
%dir %{_includedir}/phonenumbers/base
%dir %{_includedir}/phonenumbers/base/memory
%dir %{_includedir}/phonenumbers/base/synchronization
# dir %{_includedir}/phonenumbers/geocoding
%dir %{_includedir}/phonenumbers/utf
%{_includedir}/phonenumbers/*.h
%{_includedir}/phonenumbers/base/*.h
%{_includedir}/phonenumbers/base/memory/*.h
%{_includedir}/phonenumbers/base/synchronization/*.h
# {_includedir}/phonenumbers/geocoding/*.h
%{_includedir}/phonenumbers/utf/*.h
# {_libdir}/libgeocoding.so
%{_libdir}/libphonenumber.so
