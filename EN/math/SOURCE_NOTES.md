# Source inconsistencies retained in the English translation

These notes record issues noticed while translating the Chinese mathematics chapters. They are not a comprehensive mathematical or historical revision. The English chapters retain the source's mathematical expressions, examples, diagrams, and claims; this separate record distinguishes inherited issues from translation changes. References below name the Chinese source files and their original line numbers.

## Chapter 3

- `math/latex/chapters/ch03.tex:160,164`: the similarity statements list triangle vertices in an order that does not match the corresponding angles. With the given right angle at C and altitude foot D, the listed triangles are similar, but the displayed vertex order is not the correspondence order. The subsequent length identities are retained.
- `math/latex/chapters/ch03.tex:94,95`: the labels beta and gamma appear above the auxiliary parallel line, whereas the proof describes alternate interior angles below it. Diagram coordinates and label placement are unchanged.

## Chapter 4

- `math/latex/chapters/ch04.tex:180–184`: the diagram labelled `y=x^2` is plotted using `0.5*x*x`, with points `(2,2)` and `(-2,2)`. The source explicitly calls the drawing vertically compressed, but its coordinate labels do not represent the uncompressed equation.
- `math/latex/chapters/ch04.tex:296`: the discussion of `x=t^3, y=t^6` calls its locus the right half of the parabola without restating the needed nonnegative parameter domain.
- `math/latex/chapters/ch04.tex:324`: the hint suggests testing the origin to choose a side of `x+y=0`; the origin lies on that boundary and cannot distinguish the two sides.

## Chapter 5

- `math/latex/chapters/ch05.tex:7–11`: the launch point is called the coordinate origin but is then specified as `(0,2)`.
- `math/latex/chapters/ch05.tex:159`: the first polynomial graph uses a vertical factor `0.35`, while its equation label omits that factor.
- `math/latex/chapters/ch05.tex:213`: the third interpolation component is `l3(x)=1/8*x*(x-1)`; it should have coefficient `1/12` to equal one at `x=4`. The subsequent verification and claimed expanded polynomial therefore do not follow from the printed components.
- `math/latex/chapters/ch05.tex:309`: the toolbox says repeated roots bounce off the axis. Only even multiplicities bounce; odd multiplicities, including the triple-root exercise later in the chapter, cross.

## Chapter 6

- `math/latex/chapters/ch06.tex:89–95`: the definition of a symmetry transformation requires preservation of the figure but does not explicitly require an isometry. The following discussion and the eight-symmetry theorem assume distance preservation. Under the broader definition alone, a square has more than eight self-maps.
- `math/latex/chapters/ch06.tex:128`: the counting proof invokes a fixed centre before fully justifying preservation of the vertex set; its short side–side–side explanation should be read as an intuitive argument with the centre constraint included.
- `math/latex/chapters/ch06.tex:207`: an ordinary Rubik's cube cannot exchange just two edge pieces while leaving everything else fixed using legal face turns. The description also identifies operations with small support as commutators, whereas a commutator is specifically a composition of the form `aba^-1b^-1` (or its convention-dependent inverse).

## Chapter 7

- `math/latex/chapters/ch07.tex:145,273`: three planes arranged like open book pages share a spine, so this picture does not illustrate pairwise intersections with no common point.
- `math/latex/chapters/ch07.tex:227`: JPEG and streamed animation are described through low-rank/SVD-style image compression. This is an illustrative analogy, not an accurate account of those formats' standard compression methods; the quantitative compression claims are also not general guarantees.
- `math/latex/chapters/ch07.tex:231,275`: repeated matrix multiplication is said to converge in direction to the eigenvector with the largest eigenvalue without conditions. Dominance in absolute value, a suitable initial component, and other hypotheses matter. The web-ranking sketch also omits normalization/damping details needed for the claimed behaviour.
- `math/latex/chapters/ch07.tex:231`: the source calls Experiment 2 earlier even though it appears later in the chapter. The English refers to it without changing the experiment order.

## Chapter 8

- `math/latex/chapters/ch08.tex:64–66`: the displayed secants do not pass through their named pairs of plotted points, and the tangent does not pass exactly through P. Original TikZ coordinates are retained.
- `math/latex/chapters/ch08.tex:90–92`: curvature is introduced as the rate of tangent-angle change without clarifying signed versus nonnegative curvature or the additional regularity needed beyond an existing tangent.
- `math/latex/chapters/ch08.tex:206`: the observation exercise places Beijing on latitude 60 degrees north and describes flying east toward Europe. Both geographic directions require correction for a literal real-world route.
- `math/latex/chapters/ch08.tex:213`: the area hint asks whether one-eighth of a sphere consists of four or eight such triangles. The intended comparison is with the whole sphere; the stated triangle itself already occupies one-eighth.
- `math/latex/chapters/ch08.tex:220`: the arrow-carrying exercise mixes parallel transport with turning the arrow to follow the triangle's edges. An arrow deliberately turned to remain forward-facing does not obey the parallel-transport rule whose final rotation is measured by spherical excess.

## Chapter 9

- `math/latex/chapters/ch09.tex:61–68`: the `n=8` partial sum is printed as `11.111111` rather than `11.1111111`; its stated error corresponds to the latter. The following sentence says every two added terms produce another zero in the gap, whereas this decimal geometric sequence gains one zero per added term.
- `math/latex/chapters/ch09.tex:150–152`: the diagram's dashed corridor boundaries are not symmetric about the point labelled 1, despite the caption.
- `math/latex/chapters/ch09.tex:254`: the least-upper-bound formulation omits the requirement that the set be nonempty.
- `math/latex/chapters/ch09.tex:295`: eight bisections of `[1,2]` leave an interval of width `1/256`; they do not by themselves establish three-decimal-place accuracy for the displayed approximation `1.414`.

## Chapter 10

- `math/latex/chapters/ch10.tex:235`: the connection box describes Chapter 2's slope as a constant-function special case; the intended statement concerns a linear function's constant derivative.
- `math/latex/chapters/ch10.tex:267–270`: the zero-derivative corollary is stated before the mean value theorem and explicitly left without proof, as in the source.
- The derivative formulas, optimization examples, and original tangent diagram are retained without changes to their mathematical expressions.

## Chapter 11

- `math/latex/chapters/ch11.tex:89–93,307`: the integral of velocity is identified as total distance without initially distinguishing signed velocity from nonnegative speed. The observation exercise later revisits this distinction. Signed integration gives displacement; distance requires speed.
- `math/latex/chapters/ch11.tex:106–122`: the fundamental-theorem proof passes from individual local approximations to a limit of their sums without establishing uniform error control. It is an intuitive proof sketch, as its introduction indicates.
- `math/latex/chapters/ch11.tex:203`: density values are correctly distinguished from point probabilities for continuous distributions, but the prose saying probabilities belong only to intervals is broader than warranted; probabilities are defined for more general events.
- `math/latex/chapters/ch11.tex:314`: identifying `integral_a^b x dx` with the area of a trapezoid needs appropriate nonnegative bounds. It does not hold as an unsigned area statement for arbitrary a and b.

## Chapter 12

- `math/latex/chapters/ch12.tex:70`: an ascent from 100 to 1500 metres is said to pass through an altitude of `sqrt(500)` metres. That altitude is below 100; the earlier temperature example legitimately uses the same number between 10 and 25.
- `math/latex/chapters/ch12.tex:75`: bisection is described as locating the only half where a zero can lie. A sign-changing half guarantees a zero, but does not exclude additional zeros in the other half.
- `math/latex/chapters/ch12.tex:150–154`: the displayed six-term approximation to e is approximately 2.7167, but the following prose calls it five terms and claims three-decimal-place accuracy.
- `math/latex/chapters/ch12.tex:168,178–182`: the Fourier diagram is labelled as a sum of five terms but plots only the first three odd harmonics. Its dashed square-wave height is 1.25 rather than the expansion's 1. The claim that edge ripples simply get smaller omits persistent Gibbs overshoot; convergence at the jump points also needs qualification.
- `math/latex/chapters/ch12.tex:216`: matching every derivative at zero is presented as verification of the sine and cosine series. That argument needs analyticity or a Taylor-remainder estimate; matching derivatives alone does not establish equality for arbitrary smooth functions.

## Chapter 13

- `math/latex/chapters/ch13.tex:5`: the opening changes from second-year middle-school pupils to sixth-grade classes within one paragraph.
- `math/latex/chapters/ch13.tex:7`: the stated remainders when dividing 47 by 2, 3, 4, 5, and 6 are all called one. In fact they are 1, 2, 3, 2, and 5.
- `math/latex/chapters/ch13.tex:17`: trial division up to the square root is called the only reliable primality test. It is one valid method, not the only one.
- `math/latex/chapters/ch13.tex:120`: `lcm(a,b)*gcd(a,b)=ab` is stated for integers generally; standard nonnegative gcd/lcm conventions require `abs(ab)`, or positive inputs.
- `math/latex/chapters/ch13.tex:218`: after correctly describing adjacent transpositions with weight difference one, the text claims modulo 10 would miss a swap of digits differing by five. Such an adjacent swap changes the sum by five, which is detected modulo 10; missing transpositions require other weight differences. The ISBN scheme detects errors but does not by itself correct them.
- `math/latex/chapters/ch13.tex:229`: the factoring time is compared with the age of the universe without a specified algorithm, machine, or estimate. RSA security is also simplified to factoring and does not cover practical encoding/padding requirements. The toy example and source claim are retained, not presented as implementation advice.

## Chapter 14

- `math/latex/chapters/ch14.tex:31`: at one arrangement per second, `25!` seconds is tens of millions of universe ages, not the source's hundreds of billions.
- `math/latex/chapters/ch14.tex:37`: the multiplication principle needs the stated number of second-step choices to remain available for each first-step choice; the informal wording does not explicitly state this condition.
- `math/latex/chapters/ch14.tex:161,165`: listing permutations is described as `O(n!)` without accounting for the cost of outputting n entries per permutation. The discussion also treats upper-bound notation as if it necessarily implied a lower bound or inherent infeasibility.
- `math/latex/chapters/ch14.tex:165,175`: the descriptions of travelling-salesman and factoring algorithms as essentially enumeration are loose. Known exact travelling-salesman algorithms improve substantially on factorial enumeration, and classical factoring has subexponential methods. The unresolved P versus NP question concerns polynomial-time solution versus verification, not merely improvement over enumeration.

## Chapter 15

- `math/latex/chapters/ch15.tex:116,123`: the ratio is said never to turn back as it approaches one, although the displayed first two values increase from 1.15 to 1.16. Asymptotic convergence does not assert monotonicity.
- `math/latex/chapters/ch15.tex:140`: the thousand-composite construction is called astronomically long; its location is astronomical, but its length is only one thousand integers.
- `math/latex/chapters/ch15.tex:217,219`: counts of verified zeros and the Earth–Moon analogy are source-era illustrative claims, not independently updated measurements. The Riemann-hypothesis error bound concerns the logarithmic-integral approximation, not the coarser `x/log(x)` approximation discussed earlier.
- `math/latex/chapters/ch15.tex:245`: the mean consecutive-prime gap below 100 is `(97-2)/24`, approximately 3.96, not 4.3.
- `math/latex/chapters/ch15.tex:278`: the logarithm-of-product hint suppresses the minus sign in `-log(1-p^-s)`; the positive leading reciprocal term arises with that minus sign included.

## Chapter 16

- `math/latex/chapters/ch16.tex:29–40,55,83`: the seven-bridges drawing has degrees A=5, B=4, C=3, D=2, not the stated 5,3,3,3. Its two odd vertices allow an open Euler trail, contradicting the subsequent claim that this drawing has four odd vertices. The original TikZ edges and the original prose counts are both retained.
- `math/latex/chapters/ch16.tex:69`: theorem item 2 allows a route that need not return but requires exactly two odd vertices. With that wording, zero odd vertices must also be allowed; exactly two is correct for distinct endpoints.
- `math/latex/chapters/ch16.tex:99`: the letter classification is not a homeomorphism classification. A, D, O, P, Q, and R can share a loop count while differing in endpoints and branch points; E also differs from T and Y as a thin-line graph. Font conventions further affect these examples.
- `math/latex/chapters/ch16.tex:135–149`: Euler-characteristic counts require suitable cell subdivisions, with disc-like faces; an arbitrary connected graph on a torus does not suffice. The formula `chi=2-2g` requires closed connected orientable surfaces. The planar proof counts bounded regions only, despite initially describing plane regions without clearly excluding the unbounded one.
- `math/latex/chapters/ch16.tex:156`: cutting a Mobius strip along its centre produces a longer band with two full twists under the usual ribbon-twist convention, not the source's one full twist.
- `math/latex/chapters/ch16.tex:7,9,45,47,83,99,110,154,168,170`: Markdown-style double asterisks appear literally in the LaTeX source. They are retained rather than converted into new styling commands.

## Chapter 17

- `math/latex/chapters/ch17.tex:99–103`: spherical sections must be normal sections through the centre to all be great circles. A cylinder's intrinsic geometry agrees locally, not globally in every measurement, with the plane.
- `math/latex/chapters/ch17.tex:117`: the historical dating of the spherical triangle area formula to the early nineteenth century is too late; the formula is associated with Girard's seventeenth-century work.
- `math/latex/chapters/ch17.tex:171`: a 3500-kilometre saving is not more than a Beijing–Urumqi round trip.
- `math/latex/chapters/ch17.tex:199`: the intrinsically flat torus obtained by identifying rectangle sides is an abstract metric quotient; an ordinary smooth doughnut surface in three-dimensional space is not an isometric realisation of that flat metric.
- `math/latex/chapters/ch17.tex:246–248`: with a 120-degree longitude difference, the triangle's angles are 120,90,90 degrees, not three equal angles as the hint claims.
- `math/latex/chapters/ch17.tex:260–262`: the great-circle intersection claim needs the circles, and hence their defining planes, to be distinct.
- `math/latex/chapters/ch17.tex:266–268`: the side–side–side challenge needs a convention for minor arcs and the chosen interior region. Standard nondegenerate minor-arc spherical triangles do obey side–side–side congruence.

## Chapter 18

- `math/latex/chapters/ch18.tex:17,52–56`: the birthday calculation assumes independent birthdays as well as uniformity. The frequency-based probability definition is intuitive rather than an axiomatic definition; a rigorous treatment distinguishes limits of random frequencies from the probability measure itself.
- `math/latex/chapters/ch18.tex:85`: Bayes' formula also requires `P(A)>0`; the statement only specifies positive probabilities for the partition events.
- `math/latex/chapters/ch18.tex:153`: with full marks 100 and failure below 60, half full marks and half failing cannot average exactly 80.
- `math/latex/chapters/ch18.tex:151,158,171`: universal claims about negative player expectation, the equivalence of high risk with high expected returns, and nearly deterministic aggregate insurance payouts are simplified, conditional illustrations rather than unrestricted guarantees.
- `math/latex/chapters/ch18.tex:176`: the central limit theorem is stated without centring/scaling, finite-variance or comparable hypotheses, or restrictions preventing one contribution from dominating. Independence alone does not imply normal convergence for arbitrary distributions.
- `math/latex/chapters/ch18.tex:242`: blind pencil marks are not guaranteed to be uniform in the square, and rejecting marks outside the paper is not the same as rejecting marks outside the square. Pooling observations improves statistical precision under the model but need not improve each realised estimate.

## Chapter 19

- `math/latex/chapters/ch19.tex:13–15,55,264`: `2^68` is approximately 2.95e20, whereas the Chinese verbal number is three hundred-million squared, 3e16 (thirty quadrillion). Both the displayed bound and inconsistent verbal count are retained. The final claim of checking that many values in a blink is likewise unsupported. Verification bounds and record-prime descriptions are source-era claims, not updated records.
- `math/latex/chapters/ch19.tex:25`: the prime list following `n=4,5,6,...` starts with the values for n=2 and n=3, misaligning inputs and outputs.
- `math/latex/chapters/ch19.tex:37–39`: the Polya-conjecture history compresses the 1958 disproof and later identification of the least counterexample into one account.
- `math/latex/chapters/ch19.tex:125–129`: incompleteness is described as having appeared earlier, but its full discussion is in the following chapter. The argument from completeness to a halting decider also needs effective axiomatisation and appropriate consistency/soundness conditions; completeness alone is insufficient.
- `math/latex/chapters/ch19.tex:139,234`: the binary-search bounds omit rounding/final-comparison conventions. Finding a target among 16 positions can require a fifth equality comparison; four comparisons can identify it if the sole remaining candidate is inferred without checking. The later exercise gives the safer ceiling-plus-one bound.
- `math/latex/chapters/ch19.tex:143–150`: P and NP formally classify decision problems with specified input encodings. The Sudoku illustration needs variable-size generalisation, and polynomial time is an asymptotic category, not an unconditional practical speed guarantee.
- `math/latex/chapters/ch19.tex:179–183`: plotted growth curves are explicitly schematic; the final exponential coordinate is not a value of the preceding scaled exponential curve.

## Chapter 20

- `math/latex/chapters/ch20.tex:52`: enumerating positive fractions needs duplicate removal, then inclusion of zero and negative rationals, to establish the claimed bijection with all rationals. Those steps are implicit, not stated in the source.
- `math/latex/chapters/ch20.tex:69–71,85`: the infinite decimal diagonal proof needs a digit convention avoiding alternative expansions such as trailing nines versus terminating decimals. Simply changing digits can produce a different expansion of the same real number; the finite five-digit experiment does not resolve that infinite issue.
- `math/latex/chapters/ch20.tex:132`: the informal Godel argument moves directly from proving a false statement to inconsistency. General consistency is not the same as arithmetic soundness; the actual incompleteness argument uses the special provability encoding and appropriate formal hypotheses.
- `math/latex/chapters/ch20.tex:135`: continuum-hypothesis independence from ZFC is conditional on consistency of the underlying theory. Calling it an instance of a specifically true-but-unprovable statement also suppresses questions of model and interpretation. The fifty-year chronology between Godel's coding and computer self-analysis is not a literal historical dating.
- `math/latex/chapters/ch20.tex:202–204`: the least-time/least-action discussion is an introductory simplification. General variational principles concern stationary values and do not universally imply a minimum; arbitrary variational optimisation is not continuous greedy optimisation.
