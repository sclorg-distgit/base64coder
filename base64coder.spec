%global pkg_name base64coder
%{?scl:%scl_package %{pkg_name}}
%{?maven_find_provides_and_requires}

%global long_ver  2010-12-19

Name:           %{?scl_prefix}%{pkg_name}
Version:        20101219
Release:        10.9%{?dist}
Summary:        Fast and compact Base64 encoder/decoder Java library
License:        EPL or LGPLv2+ or GPLv2+ or ASL 2.0+ or BSD
BuildArch:      noarch
URL:            http://www.source-code.biz/%{pkg_name}/java/
Source0:        http://repo2.maven.org/maven2/biz/source_code/%{pkg_name}/%{long_ver}/%{pkg_name}-%{long_ver}-distribution.zip

BuildRequires:  %{?scl_prefix_java_common}maven-local
BuildRequires:  %{?scl_prefix}mvn(org.sonatype.oss:oss-parent:pom:)
BuildRequires:  %{?scl_prefix}mvn(org.apache.felix:maven-bundle-plugin)

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
%{?scl:scl enable %{scl} - <<"EOF"}
set -e -x
sed -i 's/\r//g' README.txt CHANGES.txt
%mvn_file : %{pkg_name}
%{?scl:EOF}

%build
%{?scl:scl enable %{scl} - <<"EOF"}
set -e -x
%mvn_build
%{?scl:EOF}

%install
%{?scl:scl enable %{scl} - <<"EOF"}
set -e -x
%mvn_install
%{?scl:EOF}

%files -f .mfiles
%doc README.txt CHANGES.txt

%files javadoc -f .mfiles-javadoc

%changelog
* Thu Jan 15 2015 Mikolaj Izdebski <mizdebsk@redhat.com> - 20101219-10.9
- Rebuild to fix provides

* Wed Jan 14 2015 Mikolaj Izdebski <mizdebsk@redhat.com> - 20101219-10.8
- Fix BR on sonatype-oss-parent

* Tue Jan 13 2015 Michael Simacek <msimacek@redhat.com> - 20101219-10.8
- Mass rebuild 2015-01-13

* Tue Jan 06 2015 Michael Simacek <msimacek@redhat.com> - 20101219-10.7
- Mass rebuild 2015-01-06

* Mon May 26 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 20101219-10.6
- Mass rebuild 2014-05-26

* Wed Feb 19 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 20101219-10.5
- Mass rebuild 2014-02-19

* Tue Feb 18 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 20101219-10.4
- Mass rebuild 2014-02-18

* Mon Feb 17 2014 Michal Srb <msrb@redhat.com> - 20101219-10.3
- SCL-ize BR/R

* Thu Feb 13 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 20101219-10.2
- Rebuild to regenerate auto-requires

* Tue Feb 11 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 20101219-10.1
- First maven30 software collection build

* Fri Dec 27 2013 Daniel Mach <dmach@redhat.com> - 20101219-10
- Mass rebuild 2013-12-27

* Fri Jun 28 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 20101219-9
- Rebuild to regenerate API documentation
- Resolves: CVE-2013-1571

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
