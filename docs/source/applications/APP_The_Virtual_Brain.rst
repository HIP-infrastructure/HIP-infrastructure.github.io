The Virtual Brain
******************

The Virtual Brain (TVB) offers software for constructing, simulating and analysing brain network models including the TVB simulator;
magnetic resonance imaging (MRI) processing pipelines to extract structural and functional brain networks;
combined simulation of large-scale brain networks with small-scale spiking networks;
automatic conversion of user-specified model equations into fast simulation code; simulation-ready brain models of patients and healthy volunteers;
Bayesian parameter optimization in epilepsy patient models; data and software for mouse brain simulation;
and extensive educational material ([Sanz_Leon_2013]_, [Schirner_2022]_).

Official resources
===================

	
	* `TVB website <https://www.thevirtualbrain.org/tvb/zwei>`_ 
	* `TVB download <https://www.thevirtualbrain.org/tvb/zwei/brainsimulator-software>`_ 
	* `TVB App GitHub <https://github.com/ins-amu/hip-tvb-app>`_
	* `TVB Pipeline GitHub <https://github.com/ins-amu/tvb-pipeline>`_
	* `The Bayesian Virtual Epileptic Patient GitHub <https://github.com/ins-amu/BVEP>`_
	
How to start The Virtual Brain on the HIP 
===========================================

.. important::

   These configuration steps must be performed each time the TVB app is started. These steps will be automated in the future.
   
Start the TVB app in a new :doc:`Desktop</guides/GUIDE_How_to_use_Desktops_and_run_applications_from_the_App_Catalog>`. A terminal should appear.
In the terminal type the following commands:

.. code-block:: console

	source /apps/tvb/conda/bin/activate
	python -m ipykernel install --user --name tvb
	jlab

Those commands will ensure that the TVB libraries are found and will then start the JupyterLab interface.
	
.. figure:: /applications/art/APP_The_Virtual_Brain/APP_TVB_commands.png
	:width: 600px
	:align: center

	**TVB's terminal.** Starting the TVB app will launch a terminal that will be used to configure the application.
	
A "JupyterLab Server Configuration" pop-up should appear asking for extra configuration steps. Click on the "Select Python path" button in order to navigate and select the correct 
Python environment located in */apps/tvb/jlabserver/bin/python*. Once selected, click the "Apply and restart" button.

.. figure:: /applications/art/APP_The_Virtual_Brain/APP_TVB_path.png
	:width: 600px
	:align: center

	**Select Python environment.** JupyterLab will ask which Python environment to use. Once specified, click the "Apply and restart" button.
	
The JupyterLab interface should restart and it is now possible to interact with notebooks which have access to the full set of TVB libraries.
	
.. figure:: /applications/art/APP_The_Virtual_Brain/APP_TVB_jlab.jpg
	:width: 600px
	:align: center

	**Jupyter Notebook.** Use notebooks to process data with The Virtual Brain.
	

For additional information regarding notebooks, please consult the official `Jupyter Notebook Documentation <https://jupyter-notebook.readthedocs.io/en/latest/>`_.
	


References
===========

.. [Sanz_Leon_2013] Sanz Leon P, Knock SA, Woodman MM, Domide L, Mersmann J, McIntosh AR, Jirsa V. The Virtual Brain: a simulator of primate brain network dynamics. Front Neuroinform., 2013, 7:10.

.. [Schirner_2022] Schirner M, Domide L, Perdikis D, Triebkorn P, Stefanovski L, Pai R, Prodan P, Valean B, Palmer J, Langford C, Blickensdörfer A, van der Vlag M, Diaz-Pier S, Peyser A, Klijn W, Pleiter D, Nahm A, Schmid O, Woodman M, Zehl L, Fousek J, Petkoski S, Kusch L, Hashemi M, Marinazzo D, Mangin JF, Flöel A, Akintoye S, Stahl BC, Cepic M, Johnson E, Deco G, McIntosh AR, Hilgetag CC, Morgan M, Schuller B, Upton A, McMurtrie C, Dickscheid T, Bjaalie JG, Amunts K, Mersmann J, Jirsa V, Ritter P. Brain simulation as a cloud service: The Virtual Brain on EBRAINS. Neuroimage., 2022, 251:118973.
