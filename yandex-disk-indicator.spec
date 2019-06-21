Summary:	Panel indicator for YandexDisk CLI client for Linux
Name:		yandex-disk-indicator
Version:	1.11.0
Release:	1
Group:		Communications
License:	GPLv3
Url:		https://github.com/slytomcat/yandex-disk-indicator/wiki
Source0:	https://github.com/slytomcat/yandex-disk-indicator/archive/%{version}.tar.gz?/%{name}-%{version}.tar.gz
Requires:	libappindicator-gtk3
Requires:	python3-inotify
BuildArch:	noarch

%files -f %{name}.lang
%doc LICENSE
%{_bindir}/*
%{_datadir}/applications/*
%{_datadir}/yd-tools

#----------------------------------------------------------------------

%description
Panel indicator for YandexDisk CLI client for Linux

%prep
%setup -q

%build
pushd build
export TARGET="yd-tools/usr"
./prepare.sh
popd

%install
cp -r build/yd-tools/usr %{buildroot}
chmod 644 %{buildroot}%{_datadir}/applications/*

%find_lang %{name}

%changelog
* Fri Jun 21 2019 Evgeny Lensky <surfernsk@gmail.com> - 1.11.0-1
- Release 1.11.0

* Sun May 12 2019 Evgeny Lensky <surfernsk@gmail.com> - 1.10.9-1
- init
