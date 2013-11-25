--- a/setup.py
+++ b/setup.py
@@ -53,8 +53,6 @@
             data_files.append(('/etc/init',
                                ['debian/upstart/diamond.conf']))
         if distro in ['centos', 'redhat', 'debian']:
-            data_files.append(('/etc/init.d',
-                               ['bin/init.d/diamond']))
             if distro_major_version >= '6' and not distro == 'debian':
                 data_files.append(('/etc/init',
                                    ['rpm/upstart/diamond.conf']))
