# Potential source inconsistencies

These notes record potential inconsistencies noticed during translation, not a comprehensive independent fact-check. The English chapters preserve the Chinese source's claims, calculations, examples, and formulas. References below identify sections in `phy/latex/chapters/`; line numbers may change as the source evolves. Editorial correction, if desired, should be handled separately from translation.

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
