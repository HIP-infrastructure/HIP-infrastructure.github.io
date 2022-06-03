How to use Desktops and run applications from the App Catalog 
**************************************************************

.. figure:: /guides/art/GUIDE_How_to_use_Desktops_and_run_applications_from_the_App_Catalog/GUIDE_desktops_header.png
	:width: 600px
	:align: center

	**Desktops on the HIP.** *Desktops are persistent environments used to run applications from the App Catalog.*

About this tutorial
====================

Objective
---------

The objective of this guide is to introduce HIP users to Desktops and how to use them 
in order to run the various applications available in the App Catalog.

This guide briefly describes the basic principles of Desktops on the HIP, which are illustrated in a short
demonstration video explaining how to: 

	* create, display, pause/resume and switch between Desktop environments
	* start one or several applications simultaneously in a Desktop environment

This guide also explains essential rules regarding data accessibility and persistence inside a Desktop environment.  

Scope 
------

This guide focuses on how to create and operate Desktops. It does not cover the uses of the various applications available in the App Catalog.
In this perspective, the *HIP APPS* and *HIP TUTORIALS* sections accessible in the sidebar menu contain documentation, tutorials and
links to external resources.

Use Desktops and run applications from the App Catalog
=======================================================

Desktops are remote virtual computers running on a secure infrastructure where HIP users can launch applications from the App Catalog
to work on their data. 
They operate similarly to a personal computer and support most common features such as: drag and drop, a clipboard, a fullscreen mode, a virtual keyboard.

Any application from the App Catalog, regardless if it is GUI- or CLI- based, can be launched in a Desktop environment.
Desktops are available in all 3 HIP spaces: the private, collaborative and public spaces, and work in a similar way.

Desktops and data persistence
-----------------------------

Once it has been initiated, a Desktop will persists until it is manually terminated. HIP users can log off and/or close their web browser and
the pending Desktops will remain accessible and unaltered.

The applications running in a Desktop environment have access to the HIP user's private space data under the */home/<HIP_USER>* directory.
It is important to note that any data and/or configuration file outside the */home/<HIP_USER>* directory will be lost when the application is closed
as */home/<HIP_USER>* is the only persistent directory, tied to the HIP user's private space at application startup.

Demonstration video
--------------------

The following demonstration video (3'30'') serves as an introduction to Desktops and shows how to run applications from the App Catalog:  

.. raw:: html

   <center>	
   <video width="680"  poster="todo.png" controls>
   <source src="todo.mp4" type="video/mp4">
   Your browser does not support the video tag.
   </video>
   </center>
	
|






