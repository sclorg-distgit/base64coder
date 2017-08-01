%{?scl:%scl_package base64coder}
%{!?scl:%global pkg_name %{name}}

%global long_ver  2010-12-19

Name:           %{?scl_prefix}base64coder
Version:        20101219
Release:        17.1%{?dist}
Summary:        Fast and compact Base64 encoder/decoder Java library
License:        EPL or LGPLv2+ or GPLv2+ or ASL 2.0+ or BSD
BuildArch:      noarch
URL:            http://www.source-code.biz/%{pkg_name}/java/
Source0:        http://repo2.maven.org/maven2/biz/source_code/%{pkg_name}/%{long_ver}/%{pkg_name}-%{long_ver}-distribution.zip

BuildRequires:  %{?scl_prefix}maven-local
BuildRequires:  %{?scl_prefix}mvn(junit:junit)
BuildRequires:  %{?scl_prefix}mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  %{?scl_prefix}mvn(org.apache.maven.plugins:maven-assembly-plugin)
BuildRequires:  %{?scl_prefix}mvn(org.apache.maven.plugins:maven-source-plugin)
BuildRequires:  %{?scl_prefix}mvn(org.sonatype.oss:oss-parent:pom:)

%description
Base64Coder is a fast and compact Base64 encoder/decoder class.

There is no Base64 encoder/decoder in the standard Java SDK class
library.  The undocumented classes sun.misc.BASE64Encoder and
sun.misc.BASE64Decoder should not be used.

%package javadoc
Summary:        API documentation for %{pkg_name}

%description javadoc
This package contains %{summary}.

%prep
%setup -q -n %{pkg_name}-%{long_ver}
sed -i 's/\r//g' README.txt CHANGES.txt
%mvn_file : %{pkg_name}
%pom_remove_plugin :maven-javadoc-plugin

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc README.txt CHANGES.txt

%files javadoc -f .mfiles-javadoc

%changelog
* Wed Jun 21 2017 Java Maintainers <java-maint@redhat.com> - 20101219-17.1
- Automated package import and SCL-ization

* Thu Feb 23 2017 Mikolaj Izdebski <mizdebsk@redhat.com> - 20101219-17
- Remove unneeded maven-javadoc-plugin invocation

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 20101219-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Jun 15 2016 Mikolaj Izdebski <mizdebsk@redhat.com> - 20101219-15
- Add missing build-requires

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 20101219-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20101219-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Jul 30 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 20101219-12
- Fix build-requires on sonatype-oss-parent

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20101219-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Mar 04 2014 Stanislav Ochotnicky <sochotnicky@redhat.com> - 20101219-10
- Use Requires: java-headless rebuild (#1067528)

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20101219-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Jun 14 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 20101219-8
- Update to current packaging guidelines

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20101219-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Feb 06 2013 Java SIG <java-devel@lists.fedoraproject.org> - 20101219-6
- Update for https://fedoraproject.org/wiki/Fedora_19_Maven_Rebuild
- Replace maven BuildRequires with maven-local

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20101219-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon May 21 2012 Stanislav Ochotnicky <sochotnicky@redhat.com> - 20101219-4
- Add maven plugins to BuildRequires

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 20101219-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Jun 07 2011 Jaromir Capik <jcapik@redhat.com> - 20101219-2
- Java suffix removed from the package name and put in the summary instead
- Version string added in the source URL (no need for manual renaming)
- POM file added in the source package -> Source1 removed (no need for copying)
- Removal of the target directory removed (not present anymore)

* Mon May 30 2011 Jaromir Capik <jcapik@redhat.com> - 20101219-1
- Initial version of the package
