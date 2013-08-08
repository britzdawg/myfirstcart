%global cartridgedir %{_libexecdir}/root/myfirstcart

Summary:       myfirst cartridge
Name:          myfirstcart
Version: 	   0.8.12
Release:       1%{?dist}
Group:         Development/Languages
License:       ASL 2.0
URL:           https://www.openshift.com
Source0:       http://mirror.openshift.com/pub/openshift-origin/source/%{name}/%{name}-%{version}.tar.gz

BuildRoot: %(mktemp -ud%{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

Requires:      rubygem(openshift-origin-node)
Requires:      openshift-origin-node-util

Obsoletes: openshift-origin-cartridge

BuildArch:     noarch

%description
DIY cartridge for openshift. (Cartridge Format V2)

%prep
%setup -q

%build
%__rm %{name}.spec

%install
%__mkdir -p %{buildroot}%{cartridgedir}
%__cp -r * %{buildroot}%{cartridgedir}

%files
%dir %{cartridgedir}
%attr(0755,-,-) %{cartridgedir}/bin/
%attr(0755,-,-) %{cartridgedir}/hooks/
%{cartridgedir}
%doc %{cartridgedir}/README.md
%doc %{cartridgedir}/COPYRIGHT
%doc %{cartridgedir}/LICENSE


%changelog
* Thu Aug 08 2013 cbritz <cbritz@vizuri.com> 0.8.12-1
- Merge branch 'master' of https://github.com/britzdawg/myfirstcart
  (britztopher@gmail.com)
- blah from mac (britztopher@gmail.com)

* Thu Aug 08 2013 cbritz <cbritz@vizuri.com> 0.8.11-1
- blah (cbritz@vizuri.com)

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

