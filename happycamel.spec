%define		subversion beta3
Summary:	Happy Camel - combine your camera with your GPS device
Name:		happycamel
Version:	v1
Release:	0.%{subversion}.1
License:	GPL
Group:		Applications
Source0:	http://dl.sourceforge.net/happycamel/%{name}-%{version}-%{subversion}.tar.gz
# Source0-md5:	16ef03495707b37acbd7a4015af37745
URL:		http://happycamel.sourceforge.net/
BuildRequires:	python-devel >= 1:2.5
BuildRequires:	rpm-pythonprov
%pyrequires_eq  python-libs
%pyrequires_eq	python-modules
Requires:	python-PIL
Provides:	python-HappyCamel
Suggests:	perl-Image-ExifTool
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Happy Camel is intended to combine your digital camera with your GPS
device. If you feed it a list of digital photos and a tracklog, it
figures out where these images were taken. It can embed this position
in the EXIF-data of your photos and create a .KMZ file for Google
Earth or Google Maps displaying your photos at the right positions
along the tracklog.

%prep
%setup -q -n %{name}-%{version}-%{subversion}

%build
python setup.py build

%install
rm -rf $RPM_BUILD_ROOT
python setup.py install \
	--optimize=2 \
	--root=$RPM_BUILD_ROOT

%py_ocomp $RPM_BUILD_ROOT%{py_sitescriptdir}
%py_comp $RPM_BUILD_ROOT%{py_sitescriptdir}
%py_postclean

rm -d $RPM_BUILD_ROOT%{_bindir}/*.py

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc BUGS README PKG-INFO
%attr(755,root,root) %{_bindir}/%{name}
%{py_sitescriptdir}/HappyCamel
%{py_sitescriptdir}/*.egg-info
