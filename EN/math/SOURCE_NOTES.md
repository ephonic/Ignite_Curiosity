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
