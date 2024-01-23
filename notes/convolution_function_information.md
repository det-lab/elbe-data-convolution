Hi Amy,

See this email below where I think my collaborator at HZDR does actually give the formula he is using. I guess what one needs to still calculate here is TOF, which is a function of the neutron energy. Classically this is just

tof = sqrt(m / (2E))*FPATH

I guess.

James

---------- Forwarded message ---------
From: Junghans, Dr. Arnd <a.junghans@hzdr.de>
Date: Wed, Aug 23, 2023 at 10:50 AM
Subject: AW: 14N+n manuscript start
To: Richard deBoer <Richard.J.deBoer.12@nd.edu>


Dear Richard,

 

yes, I it is indeed surprising that it quite strongly energy dependent. As you say, the

resonance is quite narrow at least for our short flight path.

I use as  a resolution function a simple gaussian with a width based on the RMS value

Of DTOF and DFPATH, see below.

C The FWHM from the gamma-peak width is 19.36 / 40.96  = 0.473 ns

C 19.36 ch and a time bin size of 1/40.96 ns

C divide by 2.355 to get the sigma   DTOF in nano-seconds

    DTOF = 0.2007D0 

C 5 mm scintillator fwhm and 11 mm beam spot fwhm DFPATH = DSQRT(1.1**2 + 0.5**2)/12)     

      DFPATH = 0.349D0

C units are centimetres, E is the neutron energy  

     SIGMA = E(J)* 2.D0 * DSQRT((DFPATH/FPATH)**2 +(DTOF/TOF)**2)

The flight path in our experiment is   FPATH = 867.75D0

 

As you can see the width of gamma-peak is measured in our tof spectra,

The flight path uncertainty is based on the assumption that it depends on  a uniform distribution

of the thickness of the scintillator 0.5 cm and the  lateral thickness of the neutron producing target which is 1.1 cm.

(This is not based on a measurement of the beam position, as I have no way of measuring this, but the model based on

The geometry of the setup works quite well).

 

I am still working on the flight path length.(energy shift)  Two weeks ago, we measured argon transmission

With two different flight paths from this I want to check if the flight path length is Ok.

 

Best regards

Arnd