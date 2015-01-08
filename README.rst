Raspberry Pi Shift Register Library
===================================

This is a simple(not very optimised) library to use Shift registers on a
raspberry pi.

All pin numbers are based on the GPIO.BCM numbering scheme.

All Values are automatically reversed when using the ``write`` function.

You will also need the RPi.GPIO module available.

Basic Usage
-----------

Connect the Data pin to GPIO 18, the Clock pin to GPIO 23 and the Latch
to GPIO 24.

.. code:: python

    import PiShiftPy as shift

    shift.init()
    shift.writeAll(0x00) # Will write 0000 0000
    shift.write(0xFF) # Will write 1111 1111

Advanced Usage
--------------

Writing values
~~~~~~~~~~~~~~

.. code:: python

    import PiShiftPy as shift
    shift.init(17, 27, 22, 2)  # Initialize with DataPin = GPIO17, Clock=GPIO27, Latch=GPIO22 with 2 chained registers
    shift.writeAll(0xFFFF) # Will write 0000 0000 0000 0000
    shift.writeAll(0xFFFF) # Will write 1111 1111 1111 1111

Writing individual Pins
~~~~~~~~~~~~~~~~~~~~~~~

.. code:: python

    import PiShiftPy as shift
    shift.init(17, 27, 22, 1)  # Initialize with DataPin = GPIO17, Clock=GPIO27, Latch=GPIO22 with 1 register
    shift.push_bit(0)
    shift.push_bit(1)
    shift.push_bit(0)
    shift.push_bit(1)
    shift.push_bit(1)
    shift.push_bit(1)
    shift.push_bit(0)
    shift.push_bit(1)
    shift.write_latch()

Author
------

Shrikant Patnaik
