
Name:		gitslave
Summary:		Creates a group of related repositories
Group:		Development/Other
Version:		2.0.2
Release:		1
BuildArch:	noarch
License:		LGPL 2.1
URL:		https://gitslave.sourceforge.net
Source0:		http://downloads.sourceforge.net/project/gitslave/%{name}-%{version}.tar.gz
BuildRequires:	perl
Requires:	git

%description
gitslave creates a group of related repositories—a superproject repository 
and a number of slave repositories—all of which are concurrently developed 
on and on which all git operations should normally operate; so when you 
branch, each repository in the project is branched in turn.

%files
%{_bindir}/gits
%{_mandir}/man1/*

#--------------------------------------------------------------------
%prep
%setup -q

%build
sed -i 's#/usr/local#/usr#g' Makefile
%make

%install
%makeinstall_std
