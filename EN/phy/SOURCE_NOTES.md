# Potential source inconsistencies

These notes record potential inconsistencies noticed during translation, not a comprehensive independent fact-check. The English chapters preserve the Chinese source's claims, calculations, examples, and formulas. References below identify sections in `phy/latex/chapters/`; line numbers may change as the source evolves. Editorial correction, if desired, should be handled separately from translation.

## Authorized translator safety annotations

The user subsequently approved clearly labeled, primary-source-linked safety warnings next to hazardous passages. These additions do not replace or alter translated source prose, formulas, or styles. Each is delimited in LaTeX by `BEGIN TRANSLATOR SAFETY NOTE` / `END TRANSLATOR SAFETY NOTE` comments so preservation checks can exclude only the additions. Earlier notes saying a warning decision was pending are historical; the following coverage supersedes that status.

- Chapter12: typhoon window/door advice (National Weather Service).
- Chapter13: laser experiment (FDA).
- Chapter18: railway listening and lightning-distance reassurance (Federal Railroad Administration; National Weather Service).
- Chapter20: Van de Graaff opening and concluding harmlessness claims, single-wire/ground contact, and outlet sparks (University of Colorado demonstration safety; OSHA).
- Chapter21: electrical thresholds and protective-device limitations (OSHA).
- Chapter22: battery/USB-source shorting (Energizer).
- Chapter23: induction-glass touching in opening and conclusion (GE Appliances).
- Chapter24: fluorescent-tube observation near power lines (OSHA).
- Chapter25: battery-spark experiment including its repeated foil test; microwave turntable procedure; shielding-modification puzzle; phone-in-oven puzzle/leakage inference (Energizer; FDA).
- Chapter26: sparks in opening and conclusion; sixty-degree hand immersion and its repeated explanation (CPSC; OSHA).
- Chapter27: inadequate diving-safety analogy (Divers Alert Network).
- Chapter28: aerosol discharge and blocked-pump/skin contact (EPA; Canadian Centre for Occupational Health and Safety).
- Chapter30: refrigerator sensor-bypass/open-door experiment (FDA food safety).
- Chapter32: open-fridge all-day puzzle (FDA food safety).
- Chapter33: breath-hold observation and laser experiment (Divers Alert Network; FDA).
- Chapter34: lens experiment excluding the Sun and the magnifier-burning example (NASA; London Fire Brigade).
- Chapter35: laser double-hole and hair-diffraction demonstrations (FDA).
- Chapter36: outdoor polarization and sunglasses/solar-viewing distinction; nighttime tinted-lens driving puzzle (NASA; Highway Code Rule94).

Sources were checked online during annotation. These targeted warnings are not a comprehensive safety certification of all activities in the source.

## Chapter 1

- Measurement/estimation discussion: potential issues in statements about means and uncertainties, and the observational precision needed to treat Earth as a point. Preserved pending review.

## Chapter 2

- Scale and estimation examples: the simplified Mars-probe and Gimli-glider accounts, passenger count, sand-versus-stars conclusion, semiconductor process-size description, and some dimensional examples merit review. These were preserved; this is not a verified errata list.

## Chapter 3

- Graph discussion says compressing the vertical axis makes a graph steeper. Some diagram slopes also appear inconsistent with the surrounding description.

## Chapter 4

- Shadow example uses a cosine with an angle described relative to the light, and says a vertical pencil has no shadow under horizontal light.
- Rain example calls the resultant forward-and-down after previously describing it as backward-and-down.
- A reference describes Chapter 6 material as already covered.

## Chapter 5

- Final train exercise hint subtracts rather than adds the train length.
- Highest-point discussion associates zero acceleration with remaining stopped indefinitely; relevant assumptions may need clarification.

## Chapter 6

- A prose acceleration has units of “28 meters per second.”
- Claims about weight disappearing in space and applying `F = dp/dt` directly to changing-mass systems merit qualification.
- Heavier-cup friction discussion appears to omit the dependence on normal force.

## Chapter 7

- The prediction section announces three questions but gives four.
- Simplified rubber, friction, and drag claims have been retained without independent validation.

## Chapter 8

- Tide discussion appears to generalize semidiurnal tides to all locations.
- Shell-theorem discussion extends its claim to a Hooke-type force without adequate qualification.
- Linear interior-Earth gravity omits the density assumption.
- Inverse-cube sensitivity is described using an additional square.

## Chapter 9

- Launcher range, speed, and energy statements appear internally inconsistent.
- The two-bullet wooden-block example has inconsistent premises/conclusions.
- 1,700 meters is described as twice Mount Tai's height.
- The lunar-orbit drop example appears to ignore existing orbital velocity.

## Chapter 10

- Coin-collision discussion says two outgoing coins move more slowly while retaining a fixed total quantity; the stated model warrants review.
- The train momentum comparison describes a speed as 2,000 times the speed of sound; the arithmetic appears inconsistent.

## Chapter 11

- Opening, predictions, experiment, model failure, and concluding explanation repeatedly assign the stop-and-release egg “revival” demonstration to a boiled egg. The familiar demonstration uses the still-moving contents of a raw egg; the source instead proposes slipping solid yolk/white. Cooked/raw wording is preserved throughout.
- Twisting-ruler experiment says total weight is identical in all three trials, although the first uses a bare ruler and the next two add clay.
- The raw-egg explanation says angular momentum dissipates into heat, conflating it with energy.
- Bicycle discussion first cites a self-stable counter-rotating-wheel bicycle, then says gyroscopic effect, fork geometry, and rider adjustments are all indispensable.
- Stellar-collapse estimate retains `(10/7\times10^5)^2`, whose grouping does not express the intended radius ratio. The solar-mass neutron-star progenitor and associated spin estimate also merit review.
- Layout flag: the original unwrapped three-column `lll` translation/rotation comparison table was especially wide in English. At root's request, explicit left-aligned line breaks were added inside the four longest cells in the last two rows; all columns, wording, fonts, and column styles are retained for layout QA.

## Chapter 12

- **Safety-sensitive source claim:** the typhoon-roof explanation recommends ventilation through doors/windows to relieve pressure and improve roof safety. This should receive explicit editorial review before publication; it is recorded here as source text, not endorsed safety advice. Root identified contrary guidance in [NOAA-hosted hurricane preparation material](https://coast.noaa.gov/data/hes/docs/general_info/Location%20Specific/CREATING%20A%20HURRICANE%20TOLERANT%20COMMUNITY%20CITY%20OF%20VENICE.pdf) and is handling the decision about an adjacent translator warning.
- The inverted-glass explanation compares upward atmospheric force with water weight without adequately accounting for internal pressure. Its large trapped-air-bubble failure explanation also warrants review.
- The nail example previously specifies a 20-gram nail, then describes it as displacing 20 grams of water while still sinking.
- Steel elasticity example equates `2\times10^9` Pa on a square centimeter with two cars, an apparent arithmetic mismatch; the assumed one-percent elastic strain also merits qualification.
- Potential overgeneralizations include identifying all fluid forces with pressure differences, treating Pascal's principle as restricted to nearly incompressible fluids, and saying uniform high pressure cannot damage objects.

## Chapter 13

- Laser experiment aims through a vertical glass wall along paper but describes bending toward the vertical, apparently mixing this geometry with a horizontal water surface. The procedure is preserved, including its lack of a laser-eye-safety warning.
- Old-model discussion describes a vertically thrown ball as tracing a parabola, without distinguishing a time graph from its spatial path.
- Claims of longest-time concave-mirror paths and saddle-like plane-mirror detours merit geometric qualification.
- The hanging-rope discussion extends the catenary description to loaded suspension-bridge cables and spiderwebs without clarifying loading assumptions.
- The total-internal-reflection exercise says reflected light cannot reach the diver's eye; this phrasing appears to confuse the external scene with internally reflected rays.
- Claims that stationarity remains exact in the quantum world and that all nonstationary paths cancel completely are stronger than the surrounding approximation warrants.

## Chapter 14

- The prediction and double-pendulum explanation call two angles a complete instantaneous state, omitting angular velocities. Elsewhere the chapter correctly includes position and speed for a bead.
- The pendulum potential `V=-mgl\cos\theta` is described as taking the lowest point as zero, although that formula uses a different reference zero.
- Falling-body worked example gives the position derivative of `L` as positive `mg`, while its following equation implicitly uses negative `mg`.
- The first pendulum diagram retains the original `(50:3)` bob location, above the support, and original angle arc/label geometry.
- The free-falling elevator explanation says the pendulum instantly stops, without accounting for its existing angular velocity.
- Final bead exercise describes a bead threaded on a wire, then treats contact as one-sided and unable to pull it back. This appears inconsistent with the experiment's threaded bead/key-ring geometry.
- The low-starting bead race, double-pendulum unknown/equation count, unrestricted lack of closed-form solutions for chaos, and generalized-coordinate examples merit qualification.

## Chapter 15

- The old-model section calls acceleration velocity's rate of change of a rate of change; this is inconsistent with its earlier correct position-based description.
- Memoryless examples involving rolling balls, chess positions, medical monitoring, and navigation omit variables/history that can matter. The cold/rain example is a stated everyday causal intuition, not independently verified health guidance.
- Generalized momentum/skater explanation refers to an unchanged product without specifying moment of inertia as one factor.
- Statements that magnetic fields prevent a Hamiltonian from equaling total energy conflate canonical momentum's altered expression with the physical energy's value.
- Noncrossing trajectories need conditions on complete state, dynamics, and explicit time dependence; the categorical statements and exercise preserve the original lack of qualification.
- The phase-space cell estimate has a formula `3\times10^{31}` but the following Chinese verbal number “三亿亿亿亿” denotes `3\times10^{32}`. Both are translated as written. A literal minimum-area cell/fuzzy patch of area `h` is also a heuristic, not a precise general quantum-state statement.
- The categorical impossibility of Hamiltonian descriptions of damping through coordinate changes needs qualification, particularly for time-dependent formulations. Likewise, instantaneous energy contours and universally conserved Hamiltonians presume appropriate time independence.
- Layout flag: the original phase-space diagram has long right-hand state labels extending past its ellipses; coordinates and label styles are unchanged.

## Chapter 16

- The opening recommends pushing at the swing's highest point, whereas the energy section later recommends the lowest point. The latter also says the same force over the same distance does more work at higher speed, confusing distance with time.
- The final swing exercise reverses the standing/crouching sequence used in Chapter 14, and its explanation of work costs warrants review.
- The slow-motion paragraph first describes the lowest point as fast, then describes both upper and lower endpoints as slow, apparently confusing equilibrium with the lower endpoint.
- Car-suspension stiffness calculation uses a passenger-induced two-centimeter deflection with the whole car's quarter-mass load. The accompanying abdominal-organ resonance explanation of carsickness is an unverified oversimplification.
- Although the limitations correctly distinguish Tacoma flutter from ordinary resonance, the closing explanation again foregrounds vortex-driven resonance.
- Displacement-time diagram marks points at `(1.0,1.2)` and `(3.0,1.2)` above troughs of the plotted cosine. Geometry preserved.
- The spring-at-equilibrium discussion later calls the spring unstretched/original shape, although the vertical example previously correctly says equilibrium is stretched.

## Chapter 17

- The text calls `v=f\lambda` dependent on small-amplitude linearity or globally uniform speed; these restrictions are stronger than the basic phase relation requires.
- The bottle-blowing example applies the fixed-end string expression `f_n=nv/(2L)` to an air bottle, omitting different acoustic boundary conditions/Helmholtz resonance.
- The standing-wave discussion characterizes most other frequencies as disordered noise; phase and boundary conditions merit clarification.
- Stadium-wave reaction-time arithmetic is inconsistent: half-meter spacing at tens of meters per second implies hundredths, not several tenths, of a second per spectator.
- The closing speech discussion identifies a familiar person's voice with frequency alone, rather than its full spectrum/timbre.
- Sound-reflection exercise asks whether a wave inverts without distinguishing pressure from particle-displacement waves.
- Group velocity is equated universally with signal/information speed; dispersive cases need qualification.
- Claims that particles always stay local omit mean flow/drift qualifications for real water and gases; idealized wording retained.

## Chapter 18

- **Safety-sensitive source claim:** the rail-listening paragraph presents placing an ear on railway tracks as useful advance warning of a train. This is preserved source content, not endorsed behavior; root was notified for an adjacent safety-warning decision.
- **Safety-sensitive source claim:** the lightning timing paragraph says lightning beyond three kilometers means the rain will not reach the reader yet. Timing does not establish storm safety or rainfall reach; root was notified. The following cold-air distance comparison also has the sign reversed for a fixed assumed sound speed.
- Sun--Earth sound-travel estimate says 14,000 years; the stated 150 million kilometers and 340 meters per second imply roughly 14 years. The following “over ten thousand years” claim is preserved too.
- Density comparison says steel is 8,000 times denser than air; given ordinary air/steel densities this is only rough and overlarge. Sun-source audibility is categorically denied from distance alone without specifying source strength or attenuation.
- The Doppler diagram's wavefront circles and arrow annotations appear inconsistent with the stated subsonic geometry and crowded-front claim; all geometry is retained.
- Fourier spectrum diagram labels its bars intensity while their plotted ratio follows the waveform amplitudes, not their squares.
- The section describes decibels as not purely physical and as incorporating hearing perception; the unweighted intensity-level formula itself is a physical logarithmic ratio.
- Statements about shore voices becoming clearer underwater, universally better solid sound transmission, and sound never leaving the atmosphere are simplified and need qualifications.
- Solar surface vibration is described with the general term asteroseismology rather than the more specific helioseismology; translated as written.

## Chapter 19

- Source says the field grows as already charged sweater/hair layers separate, without accounting for geometry and fixed charge versus fixed potential.
- The printer-paper example says same-sign charges cause sheets to stick together, contradicting its stated like-charge repulsion.
- Point-charge divergence is explained categorically by all real charges having finite size/distribution; this is not an adequate general statement about elementary particles.
- Electrostatic equilibrium says all charge lies on a conductor surface, rather than specifying excess net charge and qualifications about cavities.
- Faraday's pail experiment is presented chiefly as a direct charge-conservation test, with simplified insertion/induction behavior.
- Balloon-surface atom count, electron-transfer fraction, Coulomb torsion-fiber history, and static-discharge engineering examples are preserved estimates/claims, not independently validated.
- The experiment labels itself entirely safe, an absolute statement requiring contextual caution near flammable material; the source itself warns about vapors and dust.

## Chapter 20

- **Safety-sensitive source claim:** boundary 1 says a grounded person is safe provided they do not touch both transmission wires simultaneously. Contact with one energized conductor can be lethal; root was notified for an adjacent safety-note decision. This source claim must not be treated as practical electrical guidance.
- **Safety-sensitive source claim:** the opening and concluding calculation categorically describe a 200-kV Van de Graaff/0.4-J discharge as harmless. Safety depends on apparatus, discharge path, current, medical circumstances, and operating procedures; root was notified.
- The danger calculation describes voltage times total charge times duration as an energy account, multiplying by time twice if charge is already the total transferred quantity.
- Electronvolt example says moving an electron from lower to higher electric potential requires positive external energy, reversing the relevant potential-energy sign.
- Charger-plug sparks are described as evidence of roughly3kV across1mm. Ordinary plugging arcs do not justify that inferred supply voltage; root was notified.
- The chapter announces three mathematical expressions but supplies four.
- Claims that any real charge has nonzero size, potential cannot be defined at all with changing magnetic fields, and capacitors do not store charge at all are stronger than the qualified physical descriptions warrant.
- Equipotential crowding is used without always specifying equal potential intervals; source point-charge diagram uses equally spaced radii instead.
- The two-positive-charge exercise asks for a path along their joining line from infinity to the midpoint without addressing passage through an ideal point charge.

## Chapter 21

- **Safety-sensitive contextual limitations:** source discusses a supposedly safe below36V threshold, touching one wire while insulated, current thresholds, grounding, and protective-device response times without comprehensive conditions. These are translated educational claims, not instructions or verified safety specifications. The source also explicitly prohibits battery shorting.
- The pencil experiment recommends leaving its brightest/lowest-resistance setting powered for a minute and touching graphite; current, power, temperature, and cell limitations are not quantified.
- Circuit diagram's bottom current arrow points from the negative-terminal side toward the bulb, opposite its prose conventional-current direction. Original geometry retained.
- Two-loop worked example uses shared-current sum with opposite shared-resistor signs in its two loop equations; source supplies no diagram clarifying a physically consistent topology. Equations preserved.
- Kettle estimate says500kJ corresponds to0.08kWh; it is about0.14kWh. Charging exercise's15Wh battery and roughly10Wh input mismatch cannot be resolved by losses, as its hint seems to suggest.
- Limits section announces four boundaries but lists five.
- Emf is called energy rather than energy per charge in one sentence, despite a preceding correct per-coulomb definition.
- Current uniformity statements need the stated single-path/steady-state conditions; the final all-electrons-drift exercise describes charge accumulation as a conservation-law violation, though accumulation itself can conserve charge.
- Free-electron rapid motion is described purely as thermal motion; metallic-electron quantum statistics and Fermi velocities are omitted.
- The Earth--Moon thought experiment references Chapter28 for the speed-of-light limit, inconsistent with the book's later relativity chapter numbering.

## Chapter 22

- **Safety-sensitive experiment (source lines37–47):** directs the reader to connect wire directly across an AA cell or a power-bank USB output for2–3seconds. Acknowledging a near short circuit and limiting time does not establish safety; this also conflicts with Chapter21's prohibition. Root notified for safety-note handling.
- Source line59 says copper has equal numbers of positive nuclei and electrons; neutrality instead concerns equal total positive and negative charge, with multiple electrons per nucleus.
- Source line172 says force, velocity, and field are always mutually perpendicular; only the force must be perpendicular to both. Its palm-and-fingers mnemonic uses the right hand where the described arrangement is the familiar left-hand motor rule, conflicting with the correct vector cross product later.
- Force magnitude, gyroradius, and period formulas use signed q without absolute values; the source then interprets a negative scalar magnitude as a direction change. All formulas remain unchanged.
- First motor figure source lines90–118 depicts in-plane forces alongside in-plane current and field, rather than forces perpendicular to their plane. Rotation geometry also conflicts with its torque explanation. All coordinates, force arrows, and styling retained. Labels beginning at x=4.5 may cause an oversized figure.
- Source line197 evaluates2×10^-7×10^8/0.1 as20; it is200. Claim that all cabinet busbar forces add in one direction is configuration-dependent.
- Source line87 and the thought experiment use one fifty-thousandth tesla, while the numerical calculation uses5×10^-5tesla. Both source estimates retained.
- Source describes all magnetic field lines as closed loops, despite Chapter24 allowing extension to infinity. Ordinary DC motors, atomic magnetism, aurora access, radiation-belt confinement, MRI, and magnetic shielding are presented in simplified or overly universal terms.
- Puzzle2, source line271, begins with opposite currents but then describes same-direction charge teams; Puzzle3 does not specify the incoming velocity direction needed to name the initial bend direction.

## Chapter 23

- **Safety-sensitive source claim (lines12,229):** says an induction cooktop's glass is only warm/not very hot while its pot boils water. Heat transferred from cookware can leave a burn hazard; root notified. The unchanged translation is not practical safety advice.
- Foil-tube experiment lines27–33 promises a several-second fall through a15cm tube made from only3–4foil layers. Thin walls and uncertain electrical contact across the overlap may make the promised eddy-current braking weak or absent.
- Line42 treats free conduction electrons as almost stationary, confusing zero average drift with microscopic motion.
- New-concept discussion initially treats every flux change, including a loop moving in a static field, as a newly created vortex electric field. The later limits section correctly distinguishes motional and transformer induction; the earlier conflation is preserved.
- Line64 says potential belongs only to electrostatics, rather than distinguishing a scalar potential from a total field that cannot be represented solely by its gradient. Vortex-field lines need not universally be closed circles.
- Lines157,201 assert that a uniformly translating coil in a steady strong field has no induction without specifying spatial uniformity or constant linked flux.
- The AC graph labels the negative flux extremum as maximum flux rather than maximum magnitude; the magnitude-form induction and self-induction equations omit absolute values/sign qualifications.
- Line191 says heat cannot directly become electric current, overlooking direct thermal-to-electrical conversion. The description of uranium being burned is the source's analogy, not literal combustion.
- Transformer/phone-charger discussion presents a simple220V-to5V44:1ratio as if directly describing typical switch-mode chargers, and describes a50Hz field as changing100times per second, conflating cycle and reversal/strain frequencies.
- Line229 explains copper/aluminum cooktop incompatibility solely by low resistivity, omitting permeability, coupling, skin effect, and appliance design.
- Flashlight claims depend on the particular storage design; not all shake/crank lights contain only a small capacitor. Its resolution says all mechanical work becomes light despite explicitly including heat in the preceding energy chain.

## Chapter 24

- Source line225 gives the wire field as5×10^-5tesla and calls it one thousandth of Earth's field; this value is comparable to the chapter's quoted geomagnetic field, not one thousandth. Equation and comparison both preserved.
- Source lines100,119,258 call charge the electric field's only source, while the chapter also discusses induced fields. This requires distinguishing divergence sources from all causes of a field, and field-line endpoints from general field geometry.
- Capacitor figure lines60–75 shows surface B bulging beyond the right plate and crossing the outgoing wire rather than clearly passing through the gap as the prose says. Its full geometry is retained.
- Source line169 applies closed-surface Gauss's law directly to the open bowl B without explicitly completing the surface or justifying omitted flux. References to an upper plate also do not match the horizontal plate arrangement in the diagram.
- Poynting explanation says electric field near the wire is approximately axial and magnetic field azimuthal, then asserts axial energy transport; those components instead give radial energy flow. The subsequent resistive-wire calculation correctly gives inward flow. Geometry, statements, and equations retained.
- Source line203 says vacuum constants should simply be replaced by material parameters in all four equations. General material electromagnetism needs polarization/magnetization and suitable constitutive relations, not this unrestricted substitution.
- Source promises to explain all three radio observations, but does not return to the AM/FM contrast or fully explain distance dependence. The informal fluorescent-tube example beneath high-voltage lines should not be read as permission to approach electrical infrastructure.
- Sunlight-field neutrality/no-sensation explanation, shielding claims, solar-sail uninterrupted operation, and universal displacement-current/circuit statements are simplified; the charged-capacitor puzzle also omits ambient fields and the radius conditions for its fixed-point comparison.

## Chapter 25

- **Safety-sensitive experiment (source lines35–47):** creates sparks by scraping a thick wire directly across an AA cell's terminals, with no separate safety instructions. This is deliberate shorting; root notified for warning handling.
- Microwave estimate and puzzles propose stopping/supporting the turntable, considering a replacement mesh slit, and testing a phone inside an explicitly unpowered old oven. These must not be treated as authority to modify shielding, interlocks, or other safety components, or as an appliance leakage test; root notified.
- Source line112 gives vacuum permeability as exactly4π×10^-7, the older SI convention; precision treatment under the redefined SI requires qualification. Formula retained.
- Line128 explains X-ray/gamma penetration by short wavelengths fitting atomic gaps; penetration instead depends on material interactions and photon energy. High-frequency penetration is not universally monotonic, and X-ray/gamma categories overlap in frequency.
- Near/far-field discussion is categorical despite antenna dimensions and observation conditions affecting the boundary. The illustrated dipole emits along its own axis, where an ideal dipole has a radiation null; original geometry preserved.
- Foil shielding is described as cancellation/reflection with no absorption; real conductors can absorb energy, and low-frequency near-field magnetic shielding is not guaranteed by thin foil.
- Last puzzle, source line271, assigns medium-wave reception to the telescoping electric antenna; many ordinary AM radios instead use an internal ferrite-loop magnetic antenna. Its AM/FM polarization explanation is therefore not generally valid.
- Source line253 announces three challenges but supplies four. The polarizer materials initially specify two pairs/sheets, then require a third polarizer. Gamma-ray archaeological dating, all signals sharing only frequency differences, and the solar-core-to-Earth direct-radiation picture are simplified source claims.
- The radiation-risk discussion distinguishes solely by frequency/chemical-bond energy and emphasizes heating below visible light; exposure intensity, time, and other interaction mechanisms are not comprehensively treated.

## Chapter 26

- **Safety-sensitive experiment (source lines33–35):** specifies water around60°C and directs immersing a hand while counting to60. This poses a scald risk despite the brief caution; root notified for explicit warning handling.
- **Safety-sensitive claim (opening and line208):** presents sparklers/welding sparks as generally noninjurious because of tiny mass, including the heading asking why sparks do not injure. Real hot-particle burns and other welding/firework hazards remain; root notified.
- Source line164 says340kJ can raise10kg of water by80degrees; using its stated heat capacity gives about8degrees, a factor-ten discrepancy. Its inline time division also lacks denominator parentheses.
- Source line197 defines temperature as the reciprocal of the derivative of internal energy with respect to entropy, reversing the usual thermodynamic relation. Wording retained; no equation supplied there.
- Puzzle1, line221, gives about30°C for equal-mass80°C iron and20°C water; its stated heat capacities imply about25.8°C.
- Source line172 describes skin radiation passing through ordinary window glass to the outdoors; ordinary glass is not transparent to most body-temperature thermal infrared, so exchange is mainly with the cold window surface. Line179 says every object's radiation spectrum depends only on temperature, an overgeneralization of the ideal blackbody result.
- The zeroth law is said to guarantee an entire room equilibrates overnight and to justify all thermometer types, including remote radiation thermometers; actual nonequilibrium conditions and instrument response require qualification.
- Q=cmΔT is introduced using only no-phase-change as a condition; heat/work exchange, constraint-dependent heat capacities, and constant-temperature heat transfer with work are omitted. Absolute-zero/no-extractable-energy wording and equating all temperature with mean kinetic energy are simplified.
- Thermal sensation is characterized as exclusively a heat-flow-rate measurement rather than a response involving skin temperature, changes, and receptor adaptation. Ceramic microwave heating and condensation/evaporation claims are also context-dependent.

## Chapter 27

- Source line35 attributes a released syringe's failure to return exactly to its original position merely to previous compression; friction, leakage, and thermal relaxation would need separate analysis. Compression-pressure comparisons require isothermal conditions, not specified in the first experiment.
- Source line151 reduces all diving-illness safety to pressure differences and breathing compressed gas, omitting decompression and gas-related hazards. This is not practical diving guidance.
- Source line189 gives relative fluctuations of order1/10trillion for10^23events; simple independent-event scaling would be about1/sqrt(10^23), with measurement time and correlations relevant. A hundred molecules does not alone imply order-one relative fluctuations for every observable/averaging interval.
- Source line202 keeps a swelling sealed bag's internal pressure near its original value despite increasing volume; the state equation requires its pressure to fall if number and temperature stay fixed.
- Source line204 describes pushing liquid molecules apart when explaining compression, and contrasts compressing spacing versus collision frequency ambiguously. The actual compressed-liquid resistance is not captured by that wording.
- Limits section source line186 announces two misuses but lists three. Liquefaction by compression is presented without a critical-temperature qualification; the density threshold and signs of real-gas deviations are simplified.
- Brownian-motion account calls the observed particles pollen and gives a categorical hundreds-of-thousands size ratio; historical particle details, particle size, and observation scale need qualification. Single impacts are not literally unable to change particle momentum.
- Room-air impact count is quoted as10^23per second per square centimeter while adjacent Chinese number words imply10^20. The English preserves both the displayed estimate and the different number-word value. The derivation calls the molecular momentum change positive2mv, treating its magnitude rather than signed change.
- Balloon equality relies on comparable membrane mechanics, not simply equal volume/temperature; helium is referred to as molecules in the source even though ordinary helium gas is monatomic. Source terminology retained.

## Chapter 28

- **Safety-sensitive source demonstrations:** line9 suggests discharging insecticide, cooling spray, or spray paint continuously for a dozen seconds to observe can cooling, without exposure/ventilation/fire cautions. The final puzzle also suggests blocking a pump outlet by hand and rapidly compressing fully. Root notified about aerosol handling; these passages are not practical safety instructions.
- Source line49 says a braking car loses hundreds of thousands of kilojoules, whereas its later1300kg/120km/h example gives about720kJ. The unit discrepancy is preserved.
- Line188 identifies one-seventh volume after adiabatic compression with a seven-atmosphere tire, conflating isothermal and adiabatic pressure ratios. The given temperature formula implies a pressure ratio near15, not7.
- Lines119,230 explain aerosol-can cooling through closed-system adiabatic expansion, despite escaping matter; evaporation of liquefied propellant, enthalpy/flow energy, and device contents matter. Rubber-band warming/cooling is introduced experimentally but never quantitatively revisited.
- Rigid volume is equated with zero work without excluding shaft/electrical work. The simple internal-energy first law omits changing bulk kinetic/potential energy unless included by system assumptions; reversible ideal-gas adiabats require more than Q=0 alone.
- Source line162 announces two estimates but gives three. The brake-pad mass/temperature allocation and pump-friction control hold some pressure-dependent friction effects fixed by assumption.
- Heat is described as an existence mode and as microscopic motion in places, despite the preceding chapter's careful process-versus-state distinction; boundary heat transfer is described only through collisions although radiation also transfers heat.
- Cosmological thought experiment acknowledges general-relativistic subtleties but still portrays global cosmological energy as a straightforward balanced first-law ledger and all isolated expansion as cooling, stronger than justified. The later free-expansion exercise correctly states ideal-gas temperature stays constant.

## Chapter 29

- Bean/sand shaking is treated as guaranteed mixing that can never segregate, ignoring granular segregation and differing particle properties. The experiment's historical claim that nobody has ever shaken mixed beans apart is unsupported and overly absolute.
- Source line159 estimates4×10^17trials with probability2^-100as roughly1/100billion; the stated numbers give approximately3×10^-13. Line161's claims that twenty-head runs are lifetime-rare and forty-head runs hopeless for all humanity depend heavily on trial rate and participation.
- Source line172 assigns a spoonful hot/cold mixing entropy of10^-3J/K without masses or temperatures, and explains entropy's J/K units in heat-capacity-like language. The formula and estimate are retained.
- Distribution narrowing should refer to relative fraction, not raw head-count width, which grows with sqrt(N). Entropy/multiplicity counting needs constraints, coarse-graining, and probability assumptions, not just visually tidy versus mixed arrangements.
- Dust collisions in water, source lines12,213, are treated as few-molecule reversible events; dust particles contain many molecules and surrounding-fluid dissipation is omitted. Universal microscopic time-reversal statements omit interactions beyond the classical model and needed field reversals.
- Recurrence statement line228 omits bounded/finite-measure and measure-preserving conditions, and its numerical room recurrence estimate is not derived. Low-entropy initial-condition dependence is raised but not resolved by counting alone.
- Biological growth is described categorically as a large decrease in the organism's thermodynamic entropy despite growth/material exchange. Black-hole maximum-entropy-at-fixed-volume and forty-orders comparisons require constraints. Maxwell-demon erasure statements need the usual information/thermodynamic assumptions.
- The two-room perfume puzzle describes room B's experiment outdoors, and its dented-ball question switches between surrounding-water and interior-gas molecules. Both source ambiguities preserved.

## Chapter 30

- **Safety-sensitive experiment (source line37):** directs taping down a refrigerator door sensor and leaving the door open for1–2hours to sustain compressor operation. Appliance controls, food temperature, energy use, and malfunction risks are not addressed; root notified for warning handling.
- Source line8's Chinese number words mean10^26kg, whereas its parenthetical ocean mass is1.4×10^21kg. Both number-word and formula values are translated as written.
- Source line56 describes ice cooling while water warms but then says water loses heat and ice gains heat, reversing its own energy transfer. Preserved.
- Line168 claims the third law follows directly from the Carnot COP formula; vanishing COP for fixed removed heat does not alone establish unattainability for a cooling body's vanishing heat capacity. Lines181,238 say refrigeration needs a colder waste-heat reservoir, opposite the chapter's own refrigerator heat flow to the warmer reservoir.
- Perfect-crystal zero entropy is labeled Nernst's formulation and unconditionally equivalent to unattainability; ground-state uniqueness and qualifications are omitted. The third law is characterized as merely another face of second-law entropy statistics, though additional assumptions are needed.
- Single-reservoir heat is said unable to produce any work, omitting the cyclic/no-other-effects qualification supplied in the formal Kelvin statement. Isothermal expansion can produce work with another state change. Ideal reversible heat concentration plus recovery can break even rather than necessarily lose work as line211 claims.
- Carnot plot's supposed isotherms do not have constantpV at their specified points; no geometry was changed. Efficiency ratios are said to define temperature ratios directly rather than using the appropriate reversible heat ratio relation.
- The50°Cwater split-and-cycle puzzle also claims work output with return to the same complete state and no net input, an energy-balance problem in addition to its second-law violation; its hint discusses only the latter.
- Open-fridge prose counts transported compartment heat plus electrical input as room heating without consistently distinguishing gross condenser heat from net whole-room gain. Whole-room net input is electrical work, plus other boundary exchanges.
- Stellar radiation's ultimate conversion ceiling is described solely by a two-reservoir Carnot bound, omitting radiation entropy/dilution and conversion assumptions. Laser-only nanokelvin cooling and black-hole laws almost word-for-word are simplified source claims.

## Chapter 31

- Ten-coin discussion says the five-and-five result competes with more than900other arrangements;1024minus252is772. Coin symmetry alone does not guarantee unbiased independent tossing, particularly for the suggested caps/buttons.
- Central-limit discussion omits variance and dependence conditions; many listed distributions are not automatically Gaussian. Relative fluctuations shrink, rather than authority growing, as1/sqrt(N), and probability above one does not specifically diagnose missed states.
- Boltzmann weights apply per microstate; probabilities of energy levels require degeneracy/density of states. The categorical high-energy-is-rarer claim also needs the positive-temperature assumption, given Chapter26's negative-temperature discussion. Free-energy minima need ensemble constraints.
- Final puzzle says microstate count is extensive and doubles when system size doubles. Counts multiply for independent subsystems; entropy is additive. The hospital-room tidiness example also conflicts with Chapter29's warning against aesthetic definitions of entropy.
- Quantum indistinguishability/Gibbs-paradox discussion, equipartition's relation to ultraviolet catastrophe, noise-voltage proportionality to temperature, and the account of the Sun's fusion timescale are simplified or potentially misleading. Activation energy changes between per-particle and molar conventions; the numerical use of R needs that distinction.
- Opening number words imply order10^19molecules, while the later estimate is10^23; source estimates preserved. Pressure fluctuation claims also need observation-time and correlation qualifications.

## Chapter 32

- Opening announces two scenes but gives three. Photo/file-size compression ratios depend on format and encoder; incompressibility statements are probabilistic, not a guarantee for every individual file.
- Shannon-entropy explanation says log2 grows as probability decreases, omitting the negative sign; the three stated qualitative requirements alone do not establish uniqueness without further axioms. Physical Shannon/thermodynamic entropy conversion needs specified ensembles and correlations.
- Demon erasure heat exactly cancels extracted work only at the ideal limit; real costs can exceed it. Several claims about erasure, cyclic memory, and record-free measurement omit assumptions about logical reversibility and correlations. Brownian acceleration alone does not establish an entropy-decreasing fluctuation.
- Data-center electricity claim combines several thousand TWh with1–2percent of global consumption, an apparent numerical mismatch; Voyager's current-distance/image-transmission example also conflates historical imaging with later mission distances.
- Earth radiation entropy estimate uses an apparent Q/T approximation without the blackbody4/3factor; body-order entropy deficit is asserted without a defined comparison state. Equilibration after death is not instantaneous, and urban heating has causes beyond air-conditioner exhaust.
- The statement that a10^23-particle fluctuation probability needs more decimal zeros than visible-universe atoms is inconsistent with ordinary exponential-in-N estimates. The distinction between generic microscopic fluctuations and universal macroscopic impossibility needs qualification.
- Layout flag: the original Earth/Sun diagram has right-anchored labels beyond x=5.6 and long incoming labels; all original coordinates/options are preserved and need root's visual QA.

## Chapter 33

- Opening total-reflection scene describes above-water lights/ceiling reflected when outside scenery disappears; the later explanation correctly identifies underwater scenery. Source's contradictory wording is preserved.
- Refractive index alone does not unconditionally measure bending without specifying both media and angle. Total-internal-reflection discussion neglects evanescent fields and frustrated reflection, and reflectivity approaches rather than discontinuously jumps to unity at critical incidence.
- Ray diagram's incidence/reflection arcs do not match the drawn ray angles exactly. Optical-fiber labels lie close to the zigzag path. All geometry remains unchanged for visual QA.
- Extended fluorescent-source shadow softness is used as a diffraction example after being correctly explained as penumbra earlier. The statement that light travels straight above water but not below misstates the role of the interface in a uniform-water example.
- A stationary path may also be a non-strict minimum; equal ellipsoidal-mirror paths do not by themselves refute a minimum characterization. Statements about optical-path maxima and arbitrary ray shapes need variational/domain qualifications.
- Refraction's half-degree angular solar correction does not universally equal two minutes in sunrise/sunset time; latitude and solar declination affect the horizon crossing rate. The atmosphere's thickness and gradient claims in the globe-circling thought experiment are oversimplified.
- The mirage discussion calls a nonuniform-air case a violation of the conditional uniform-medium rule; strictly it lies outside that rule's conditions. Its continuous turning-point account is an approximation, not a literal succession of sharp interfaces.

## Chapter 34

- Opening claims mirrors never reverse up/down even when horizontal; later it correctly describes reversal normal to the surface and comparison-dependent handedness. The nose/back example uses30cm and30.4cm, an implausible body-depth difference retained verbatim.
- Principal-ray description says a ray at a spherical mirror's vertex barely changes direction; the reflection rule instead applies. Plane-mirror figure rays do not obey equal reflection angles, and the lens figure's second ray does not pass through the optical center; all coordinates preserved.
- Magnifier/virtual-image explanation says rays become more divergent, rather than the usual less-divergent output for a positive lens inside focus. The infinite-focal-length lens limit is described as a plane mirror, conflating reflection and transparent propagation/sign conventions.
- The similarity derivation uses unsigned image heights despite the earlier signed magnification convention; its small-angle explanation in terms of arc length is imprecise. Peepholes and dental mirrors are simplified and not universally a single concave lens or nonmagnifying plane mirror.
- Statements that all orientation calibration is learned, that the eye reaches the physical ceiling, and that visible microscopes cannot resolve below0.2micrometers are stronger than justified; super-resolution and detector/aberration qualifications are omitted. The oil-immersion paragraph calls increasing numerical aperture work on the numerator although it reduces the resolution denominator.
- The lunar-flag thought experiment categorically rules out future single mirrors, though its own argument only fixes the aperture requirement at a given distance/wavelength. The aperture estimate for a50kmorbiter is several centimeters; actual imaging/sampling conditions matter.
- Root wrapped the two original caption nodes with explicit line breaks to resolve English overflow, retaining geometry, styling, words, and math.

## Chapter 35

- Sunlit-shadow softness is used as evidence of diffraction without separating the Sun's extended-source penumbra. The finger-gap directional explanation alternates between the narrowed dimension and its perpendicular in potentially contradictory language.
- Thermal-source phase changes are claimed10^16times per second, faster than typical visible carrier frequencies. Coherence depends on spectral/spatial properties; double-slit interference does not require only a few wavelengths of path difference, and sunlight failure is not solely temporal path mismatch.
- Ideal point-slit limits d→0 and wavelength→0 are interpreted as uniform-screen light or two geometric slit images without retaining finite-aperture diffraction envelopes and observation-regime conditions. A wavelength-wide slit does not scatter uniformly into a sphere, and diffraction is not literally absent for a larger aperture.
- Film derivation gives soap-film destructive condition2nt=mλ, then applies quarter-wave2nt=λ/2to an antireflection coating without explaining the changed two-reflection phase shifts. Both equations and the intervening prose are preserved.
- Grating expression omits incident-angle dependence despite the oblique CD experiment; DVD spacing differs from the quoted CD value. Hair diffraction needs the relevant Babinet/Fraunhofer approximation.
- One-slit intensity is later called uniform despite the chapter's own diffraction envelope. I0in the interference equation is the maximum combined intensity, not explicitly defined as such; global energy arguments need consistent illumination/collection assumptions.
- Rayleigh resolution is presented as a universal hard limit and ocular diffraction as the only limit. Which-path measurement generally yields summed diffraction patterns, not merely two geometric patches. EHT's twenty-microarcsecond resolution is not equivalent to a coin viewed across Beijing--Shanghai.

## Chapter 36

- Opening says most sunglasses are polarized; later correctly distinguishes ordinary dark lenses. Screen experiment's one-eighth fraction is relative to unpolarized backlight before its first polarizer, not the unobstructed already-polarized screen; ideal external45°/90°sheets transmit one-quarter of that screen output.
- Experiment says suppressed asphalt glare reveals objects beneath the road surface, and describes Brewster angle without defining the normal. The rope-fence analogy is dismissed as incapable of projection, although suitable mechanical transverse constraints can exhibit analogous component selection.
- Oneline says polarizers do not delete light, though absorption/removal is essential alongside projection. An ideal polarizer transmits half unpolarized light, not the later claim of more than half underwater disordered light.
- Dispersion, absorption, and metallic reflection are oversimplified: visible light does drive bound charges off resonance, metals do not respond identically at every frequency or perfectly cancel all internal fields, and finite skin depth/absorption matter. Rayleigh scaling assumes appropriate scatterers/frequency range.
- Modern3Dsystems are not universally two-projector circular systems; ordinary cinema glasses are not always interchangeable with linear-polarizer sheets for the opening experiment. Sky polarization degree/pattern depends on viewing conditions, aerosols and multiple scattering, not a universal mostly-polarized fraction.
- Jones vectors describe fully polarized coherent states; partial polarization needs a more general description. LCD liquid-crystal layers are not absorptive middle polarizers, and the one-photon cos²transmission statement needs conditioning on its incident polarization/first-sheet passage.
