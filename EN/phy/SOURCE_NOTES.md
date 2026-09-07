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
