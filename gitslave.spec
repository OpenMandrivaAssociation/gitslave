
Name:		gitslave
Summary:	gitslave creates a group of related repositories
Group:		Development/Other
Version:	2.0.1
Release:	%mkrel 2 
BuildArch:	noarch
License:	LGPL 2.1
URL:		http://gitslave.sourceforge.net
Source0:	http://downloads.sourceforge.net/project/gitslave/%{name}-%{version}.tar.gz
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
Requires:	git

%description
gitslave creates a group of related repositories—a superproject repository and
a number of slave repositories—all of which are concurrently developed on and
on which all git operations should normally operate; so when you branch, each
repository in the project is branched in turn.

%files
%defattr(-,root,root)
%_bindir/gits
%_mandir/man1

#---------------------------------------------------------------------------------
%prep
%setup -q

%build
sed -i 's#/usr/local#/usr#g' Makefile
%make

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot
