Name: nethserver-glpi
Version: 0.1.4
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
* Sun Sep 10 2017 Stephane de Labrusse <stephdl@de-labrusse.fr> 0.1.4-1.ns7
- Restart httpd service on trusted-network

* Wed Mar 29 2017 Stephane de Labrusse <stephdl@de-labrusse.fr> 0.1.3-1.ns7
- Template expansion on trusted-network

* Mon Mar 20 2017 stephane de Labrusse <stephdl@de-labrusse.fr> 0.1.2-1.ns7
- Redirect the cron job email to /dev/null

* Sun Mar 19 2017 stephane de Labrusse <stephdl@de-labrusse.fr> 0.1.1-1.ns7
- First release to NS7

