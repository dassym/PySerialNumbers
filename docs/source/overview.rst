Overview of PySerialNumbers library
*************************************
 
The PySerialNumbers library offers functionalities for manipulating serial numbers.
In particular the possibility of reading a character string formatted according to the ad hoc :doc:`grammar <./grammar>`,
then of converting it into a list of serial numbers.


Serial number
=============

A serial number consists of 3 parts:
    
    - *The prefix*: all the characters located before the last group of digits (number)
    
    - *The number*: the last group of digits, this part can be incremented
    
    - *The suffix*: all the characters located after the last group of digits (number)

.. seealso::

	The class :class:`.SerialNumber` and the grammar rule for :a4:r:`serial number <serialnumbers.sn>`.
	
.. code::

    A001X ⇒ prefix = A ; number = 1 ; suffix = X
    
    001X ⇒ prefix = None ; number = 1 ; suffix = X
    
    A001 ⇒ prefix = A ; number = 1 ; suffix = None
    
    
Serial number range
===================

A serial number range consists of a sequence of consecutive serial numbers:      

.. seealso::

	The class :class:`.SerialNumberRange` and the grammar rule for :a4:r:`ranges <serialnumbers.range>`.

.. code:: 

	X001:10 ⇒ [SerialNumber('X001'), SerialNumber('X002'), ..., SerialNumber('X010')
	
	X001-X010 ⇒ [SerialNumber('X001'), SerialNumber('X002'), ..., SerialNumber('X010')

Serial number list
==================

A list of serial numbers allows multiple ranges of non-consecutive serial numbers to be specified.
It is possible to specify ranges to exclude by prefixing it with a "minus" sign (-).

.. seealso::

	The class :class:`.SerialNumberList`
	and grammar rule for :a4:r:`lists <serialnumbers.list>`.  

.. code:: 

	X01:10;X50-X59;-X02:2 ⇒ [SerialNumber('X01'), SerialNumber('X04'), ..., SerialNumber('X10'), SerialNumber('X50'), ..., SerialNumber('X59')]






 