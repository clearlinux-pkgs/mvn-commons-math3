#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : mvn-commons-math3
Version  : 3.4.1
Release  : 5
URL      : https://repo1.maven.org/maven2/org/apache/commons/commons-math3/3.4.1/commons-math3-3.4.1.jar
Source0  : https://repo1.maven.org/maven2/org/apache/commons/commons-math3/3.4.1/commons-math3-3.4.1.jar
Source1  : https://repo.maven.apache.org/maven2/org/apache/commons/commons-math3/3.2/commons-math3-3.2-sources.jar
Source2  : https://repo.maven.apache.org/maven2/org/apache/commons/commons-math3/3.2/commons-math3-3.2.jar
Source3  : https://repo.maven.apache.org/maven2/org/apache/commons/commons-math3/3.2/commons-math3-3.2.pom
Source4  : https://repo1.maven.org/maven2/org/apache/commons/commons-math3/3.1.1/commons-math3-3.1.1.jar
Source5  : https://repo1.maven.org/maven2/org/apache/commons/commons-math3/3.1.1/commons-math3-3.1.1.pom
Source6  : https://repo1.maven.org/maven2/org/apache/commons/commons-math3/3.4.1/commons-math3-3.4.1.pom
Source7  : https://repo1.maven.org/maven2/org/apache/commons/commons-math3/3.5/commons-math3-3.5.jar
Source8  : https://repo1.maven.org/maven2/org/apache/commons/commons-math3/3.5/commons-math3-3.5.pom
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0
Requires: mvn-commons-math3-data = %{version}-%{release}
Requires: mvn-commons-math3-license = %{version}-%{release}

%description
No detailed description available

%package data
Summary: data components for the mvn-commons-math3 package.
Group: Data

%description data
data components for the mvn-commons-math3 package.


%package license
Summary: license components for the mvn-commons-math3 package.
Group: Default

%description license
license components for the mvn-commons-math3 package.


%prep
%setup -q -n META-INF

%build

%install
mkdir -p %{buildroot}/usr/share/package-licenses/mvn-commons-math3
cp LICENSE.txt %{buildroot}/usr/share/package-licenses/mvn-commons-math3/LICENSE.txt
mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/commons/commons-math3/3.4.1
cp %{SOURCE0} %{buildroot}/usr/share/java/.m2/repository/org/apache/commons/commons-math3/3.4.1/commons-math3-3.4.1.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/commons/commons-math3/3.2
cp %{SOURCE1} %{buildroot}/usr/share/java/.m2/repository/org/apache/commons/commons-math3/3.2/commons-math3-3.2-sources.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/commons/commons-math3/3.2
cp %{SOURCE2} %{buildroot}/usr/share/java/.m2/repository/org/apache/commons/commons-math3/3.2/commons-math3-3.2.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/commons/commons-math3/3.2
cp %{SOURCE3} %{buildroot}/usr/share/java/.m2/repository/org/apache/commons/commons-math3/3.2/commons-math3-3.2.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/commons/commons-math3/3.1.1
cp %{SOURCE4} %{buildroot}/usr/share/java/.m2/repository/org/apache/commons/commons-math3/3.1.1/commons-math3-3.1.1.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/commons/commons-math3/3.1.1
cp %{SOURCE5} %{buildroot}/usr/share/java/.m2/repository/org/apache/commons/commons-math3/3.1.1/commons-math3-3.1.1.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/commons/commons-math3/3.4.1
cp %{SOURCE6} %{buildroot}/usr/share/java/.m2/repository/org/apache/commons/commons-math3/3.4.1/commons-math3-3.4.1.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/commons/commons-math3/3.5
cp %{SOURCE7} %{buildroot}/usr/share/java/.m2/repository/org/apache/commons/commons-math3/3.5/commons-math3-3.5.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/commons/commons-math3/3.5
cp %{SOURCE8} %{buildroot}/usr/share/java/.m2/repository/org/apache/commons/commons-math3/3.5/commons-math3-3.5.pom


%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/java/.m2/repository/org/apache/commons/commons-math3/3.1.1/commons-math3-3.1.1.jar
/usr/share/java/.m2/repository/org/apache/commons/commons-math3/3.1.1/commons-math3-3.1.1.pom
/usr/share/java/.m2/repository/org/apache/commons/commons-math3/3.2/commons-math3-3.2-sources.jar
/usr/share/java/.m2/repository/org/apache/commons/commons-math3/3.2/commons-math3-3.2.jar
/usr/share/java/.m2/repository/org/apache/commons/commons-math3/3.2/commons-math3-3.2.pom
/usr/share/java/.m2/repository/org/apache/commons/commons-math3/3.4.1/commons-math3-3.4.1.jar
/usr/share/java/.m2/repository/org/apache/commons/commons-math3/3.4.1/commons-math3-3.4.1.pom
/usr/share/java/.m2/repository/org/apache/commons/commons-math3/3.5/commons-math3-3.5.jar
/usr/share/java/.m2/repository/org/apache/commons/commons-math3/3.5/commons-math3-3.5.pom

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/mvn-commons-math3/LICENSE.txt
