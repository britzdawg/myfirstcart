%global cartridgedir %{_libexecdir}/root/myfirstcart

Summary:       Myfirst cartridge  
Name:          myfirstcart
Version: 	   0.8.10
Release:       1%{?dist}
Group:         Development/Languages
License:       ASL 2.0
Source0:       %{name}/%{name}-%{version}.tar.gz
Requires:      rubygem(openshift-origin-node)
Requires:      lsof
Requires:      java-1.7.0-openjdk
Requires:      java-1.7.0-openjdk-devel
%if 0%{?rhel}
Requires:      maven3
%endif
%if 0%{?fedora}
Requires:      maven
%endif
BuildRequires: git
BuildRequires: jpackage-utils
BuildArch:     noarch

%description
Provides Tomcat8 support to OpenShift



%files
%defattr(-,root,root,-)
%dir %{cartridgedir}
%dir %{cartridgedir}/bin
%dir %{cartridgedir}/hooks
%dir %{cartridgedir}/env
%dir %{cartridgedir}/metadata
%dir %{cartridgedir}/template
%dir %{cartridgedir}/versions
%attr(0755,-,-) %{cartridgedir}/bin/
%attr(0755,-,-) %{cartridgedir}/hooks/
%attr(0755,-,-) %{cartridgedir}
%{cartridgedir}/metadata/manifest.yml
%doc %{cartridgedir}/README.md


%changelog
* Thu Aug 08 2013 cbritz <cbritz@vizuri.com> 0.8.10-1
- blah (cbritz@vizuri.com)

* Thu Aug 08 2013 cbritz <cbritz@vizuri.com> 0.8.9-1
- blah (cbritz@vizuri.com)

* Thu Aug 08 2013 cbritz <cbritz@vizuri.com> 0.8.8-1
- blah (cbritz@vizuri.com)
- blah (cbritz@vizuri.com)

* Thu Aug 08 2013 cbritz <cbritz@vizuri.com> 0.8.7-1
- Merge branch 'master' of https://github.com/britzdawg/myfirstcart
  (britztopher@gmail.com)
- changed to add cart var (britztopher@gmail.com)

* Thu Aug 08 2013 cbritz <cbritz@vizuri.com> 0.8.6-1
- blah (britztopher@gmail.com)

