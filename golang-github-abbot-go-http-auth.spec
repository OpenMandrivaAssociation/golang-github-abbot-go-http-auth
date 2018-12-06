# https://github.com/abbot/go-http-auth
%global goipath         github.com/abbot/go-http-auth
%global commit          860ed7f246ff5abfdbd5c7ce618fd37b49fd3d86

%gometa

Name:           golang-github-abbot-go-http-auth
Version:        0
Release:        0.18%{?dist}
Summary:        Basic and Digest HTTP Authentication for golang http
License:        ASL 2.0
URL:            %{gourl}
Source0:        %{gosource}
Source1:        glide.lock
Source2:        glide.yaml

%description
This is an implementation of HTTP Basic
and HTTP Digest authentication in Go language.
It is designed as a simple wrapper for http.RequestHandler functions.

%package devel
Summary:       %{summary}
BuildArch:     noarch

BuildRequires: golang(golang.org/x/crypto/bcrypt)
BuildRequires: golang(golang.org/x/net/context)

%description devel
%{summary}

This package contains library source intended for
building other packages which use import path with
%{goipath} prefix.

%prep
%forgesetup
cp %{SOURCE1} %{SOURCE2} .

%install
%goinstall test.htdigest test.htpasswd glide.lock glide.yaml

%check
%gochecks

#define license tag if not already defined
%{!?_licensedir:%global license %doc}

%files devel -f devel.file-list
%license LICENSE
%doc README.md

%changelog
* Thu Oct 25 2018 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.18.20181025git860ed7f
- Bump to commit 860ed7f246ff5abfdbd5c7ce618fd37b49fd3d86

* Tue Oct 23 2018 Nicolas Mailhot <nim@fedoraproject.org> - 0-0.17.20181005gitb6a92f4
- redhat-rpm-config-123 triggers bugs in gosetup, remove it from Go spec files as it’s just an alias
- https://lists.fedoraproject.org/archives/list/devel@lists.fedoraproject.org/message/RWD5YATAYAFWKIDZBB7EB6N5DAO4ZKFM/

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.16.gitc0ef453
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 08 2018 Jan Chaloupka <jchaloup@redhat.com> - 0-0.15.gitc0ef453
- Upload glide.lock and glide.yaml files

* Mon Mar 05 2018 Jan Chaloupka <jchaloup@redhat.com> - 0-0.14.gitc0ef453
- Update to spec 3.0

* Mon Feb 26 2018 Jan Chaloupka <jchaloup@redhat.com> - 0-0.13.20140619gitc0ef453
- Autogenerate some parts using the new macros

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.12.gitc0ef453
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.11.gitc0ef453
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.10.gitc0ef453
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.9.gitc0ef453
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jul 21 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.8.gitc0ef453
- https://fedoraproject.org/wiki/Changes/golang1.7

* Mon Feb 22 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.7.gitc0ef453
- https://fedoraproject.org/wiki/Changes/golang1.6

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.6.gitc0ef453
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Sep 12 2015 jchaloup <jchaloup@redhat.com> - 0-0.5.gitc0ef453
- Update to spec 2.1
  related: #1248477

* Mon Aug 17 2015 jchaloup <jchaloup@redhat.com> - 0-0.4.gitc0ef453
- Don't provide examples
  related: #1248477

* Thu Jul 30 2015 Fridolin Pokorny <fpokorny@redhat.com> - 0-0.3.gitc0ef453
- Move test.htpasswd and test.htdigest to test unit
  related: #1248477

* Thu Jul 30 2015 Fridolin Pokorny <fpokorny@redhat.com> - 0-0.2.gitc0ef453
- Update of spec file to spec-2.0
  resolves: #1248477

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.2.gitc0ef453
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Dec 18 2014 jchaloup <jchaloup@redhat.com> - 0-0.1.gitc0ef453
- First package for Fedora
  resolves: #1175673
