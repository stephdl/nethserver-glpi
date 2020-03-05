Name: nethserver-glpi
Version: 1.0.1
Release: 1%{?dist}
Summary: Configure glpi
Source: %{name}-%{version}.tar.gz
BuildArch: noarch
URL: %{url_prefix}/%{name}
License: GPL

BuildRequires: nethserver-devtools

Requires: nethserver-httpd
Requires: nethserver-mysql
Requires: glpi

%description
Install and configure a glpi instance on NethServer

%prep
%setup

%build
%{makedocs}
perl createlinks
mkdir -p root/etc/e-smith/templates/etc/glpi/config_db.php
ln -s /etc/e-smith/templates-default/template-begin-php root/etc/e-smith/templates/etc/glpi/config_db.php/template-begin
sed -i 's/_RELEASE_/%{version}/' %{name}.json

%install
rm -rf %{buildroot}
(cd root   ; find . -depth -print | cpio -dump %{buildroot})

mkdir -p %{buildroot}/usr/share/cockpit/%{name}/
mkdir -p %{buildroot}/usr/share/cockpit/nethserver/applications/
mkdir -p %{buildroot}/usr/libexec/nethserver/api/%{name}/
cp -a manifest.json %{buildroot}/usr/share/cockpit/%{name}/
cp -a logo.png %{buildroot}/usr/share/cockpit/%{name}/
cp -a %{name}.json %{buildroot}/usr/share/cockpit/nethserver/applications/
cp -a api/* %{buildroot}/usr/libexec/nethserver/api/%{name}/


%{genfilelist} %{buildroot} > %{name}-%{version}-filelist

%files -f %{name}-%{version}-filelist
%defattr(-,root,root)
%doc COPYING
%dir %{_nseventsdir}/%{name}-update
%attr(0440,root,root) /etc/sudoers.d/50_nsapi_nethserver_glpi

%changelog
* Thu Mar 05 2020  stephane de Labrusse <stephdl@de-labrusse.fr> 1.0.1-1.ns7
- Fix bad sudoers permission

* Thu Dec 19 2019 Stephane de Labrusse <stephdl@de-labrusse.fr> 1.0.0-1.NS7
- Link in the cockpit application Page

* Sun Sep 10 2017 Stephane de Labrusse <stephdl@de-labrusse.fr> 0.1.4-1.ns7
- Restart httpd service on trusted-network

* Wed Mar 29 2017 Stephane de Labrusse <stephdl@de-labrusse.fr> 0.1.3-1.ns7
- Template expansion on trusted-network

* Mon Mar 20 2017 stephane de Labrusse <stephdl@de-labrusse.fr> 0.1.2-1.ns7
- Redirect the cron job email to /dev/null

* Sun Mar 19 2017 stephane de Labrusse <stephdl@de-labrusse.fr> 0.1.1-1.ns7
- First release to NS7
