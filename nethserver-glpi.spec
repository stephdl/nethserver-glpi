Name: nethserver-glpi
Version: 1.1.3
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

%install
rm -rf %{buildroot}
(cd root   ; find . -depth -print | cpio -dump %{buildroot})
%{genfilelist} %{buildroot} > %{name}-%{version}-filelist

%files -f %{name}-%{version}-filelist
%defattr(-,root,root)
%doc COPYING
%dir %{_nseventsdir}/%{name}-update

%changelog
* Sat Mar 18 2017 stephane de Labrusse <stephdl@de-labrusse.fr> 1.1.3.ns7
- First release to NS7

* Mon Sep 14 2015 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 1.0.1-1
- OCS Inventory LDAP authentication - Enhancement #3250 [NethServer]

* Tue Aug 25 2015 Davide Principi <davide.principi@nethesis.it> - 1.0.0-1
- Initial OCS Inventory NG package - Feature #3230 [NethServer]

* Wed Jul 22 2015 Giovanni Bezicheri <giovanni.bezicheri@nethesis.it>
- Initial version
