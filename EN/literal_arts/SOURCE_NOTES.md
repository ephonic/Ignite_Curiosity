# Source review notes

These notes distinguish questions in the Chinese source from translation
changes. They are not a comprehensive independent historical or cultural
fact-check. The English edition preserves the source's arguments, caveats,
and examples rather than silently revising them.

The source snapshot is recorded in [EN/README.md](../README.md). Chapter
references below refer to the original generated
[LaTeX source](../../literal_arts/latex/literal_book.tex), which the assembly
script can split into comparison fragments.

## Chapter 1

- The chapter describes the following “twenty-odd chapters,” although the
  complete source contains 114 chapters. This is retained in translation.
- The four cultural self-description examples are the author's broad
  generalizations, not a claim that every member of those traditions introduces
  themselves identically.
- The comparison of scientific explanation and interpretive understanding
  contains deliberately strong positions. The English preserves both sides
  and the later qualifications rather than presenting either as a consensus
  definition of science or the humanities.

## Chapter 2

- The source itself notes multiple versions of the Wang Yirong pharmacy story;
  the English retains that caveat and its selected narrative.
- The source classifies evidence by proximity to events while also warning
  that “primary” does not mean reliable. Its later classroom examples use
  broader labels for primary and secondary material. Read these together,
  rather than as an independently verified classification of every example.
- The Ötzi example's discovery date, imaging method, and account of his death
  are translated as written and remain points for a future historical review.

## Chapter 3

- References to “this year” use the source's example of 2025, not the date the
  English translation was produced. They are intentionally not updated.
- The accounts of Beijing in 1453, Babur around 1500, and the lunar/Gregorian
  dates in the Qianlong–Washington comparison merit chronological review.
  They are retained as source claims.
- The source moves between the twenty-four solar terms and the agricultural
  calendar as a whole. The English retains this explanatory simplification.

## Chapter 4

- The source describes the Berlin Conference through an expansive scene of
  drawing colonial borders. The distinction between decisions at the conference
  and later treaties or conquest is a point for independent historical review.
- The source calls its *Tribute of Yu* example three thousand years old while
  also attributing the text's composition to the Warring States period. Both
  statements are retained.
- The mathematical discussion generalizes the impossibility of flattening a
  sphere without distortion to curved surfaces generally. The latter wording
  is too broad (a cylinder's surface provides a counterexample); no mathematical
  revision has been made to the source's explanation.

## Chapter 5

- The source places the Apology's 38a statement after Socrates's death sentence;
  this placement, the detailed voting-device reconstruction, and the account of
  proposed penalties are points for a future primary-text review.
- The source's discussion of voting makes an absolute historical claim of
  universal agreement on geocentrism. The translation retains its rhetoric;
  it is not independent confirmation of that claim.

## Chapter 6

- After dating Douglass's speech to 1852, the source says Lincoln's Gettysburg
  Address came more than eighty years later. This chronology is inconsistent
  with its own reference to Lincoln invoking the 1776 founding eighty-seven
  years earlier. The erroneous interval is retained rather than silently fixed.
- The source's Atlantic-slave-trade totals move between embarkations,
  crossings, and deaths without consistently distinguishing the populations
  counted. The translation does not supply a new numerical estimate.

## Chapter 7

- The Chinese-room thought experiment and the chapter's descriptions of AI are
  translated as the source's arguments, not as a new technical assessment of
  every contemporary model. In particular, the discussion of language models as
  purely textual machines is not a claim that all AI systems lack other inputs
  or tools.

## Chapter 8

- The source's whistle analogy assumes a reed; this is not a description of
  every sports whistle. Its account of vowels also compresses the contribution
  of the vocal tract into mouth shape.
- Several original examples contain internal problems: the purported Chinese
  l/r pair instead contrasts two readings of `la`; the minimal-pair instructions
  spell “Dad” as `bā` before comparing it with `pà`; and the English `spin` /
  “phin” illustration does not consistently preserve the remaining sounds.
  These are retained as source issues rather than silently replaced examples.
- The source uses the Chinese term usually translated “phone” where its
  meaning-based definition requires “phoneme.” English uses “phoneme” for that
  defined concept. The later claim that English has no “b's meaning” conflates
  pinyin letters with phonetic sounds; English b/p are not thereby declared
  identical by this translation.
- Accounts of tone as four sections of a pitch slope, infant discrimination,
  Japanese l/r, IPA chart organization, and speech recognition are explanatory
  simplifications that merit specialist review. Historical details of the Milan
  congress, Nicaraguan signing, and Stokoe's analysis also remain source claims.
- Chinese sound examples use pinyin plus English glosses. The IPA aspiration
  mark is typeset as a superscript `h`, preserving its role without a missing
  glyph or a change to the original fonts.

## Chapter 9

- The Nix v. Hedden narrative includes dramatized scenes and detailed claims
  about import dates, witness questions, litigation costs, and fiscal motives.
  Those details require primary-record review; the English does not elevate
  the chapter's alternative explanations into findings of the court.
- The account of Rosch's work as occurring “around the same period” as
  Wittgenstein, the bird-response ordering, and the Russian blue/red comparison
  are retained explanatory claims, not newly verified experimental results.
- Word-part analyses are teaching simplifications, especially the treatment
  of Chinese `ke` as an affix and the description of all Arabic examples as
  vowel-template substitutions. Pinyin and English glosses retain the original
  Chinese examples rather than replacing them with unrelated English words.
- Clinical terms are discussed as examples of semantic drift, not as a
  diagnostic guide. The chapter's legal and age-threshold examples likewise
  are source examples, not current legal advice for all jurisdictions.

## Chapter 10

- The hunter/dog ambiguity example's stated readings do not clearly follow
  from its original Chinese word sequence. Its substitution test changes
  more than one part in one example. The translation retains these source
  problems for review rather than constructing different evidence.
- The description of French negation omits the widespread omission of `ne`
  in speech and treats the two-part construction too categorically. Claims
  that dictionaries and schools kept it unchanged also merit historical review.
- The source's assertions that Sanskrit stopped changing, that English `thou`
  disappeared completely, that humans have spoken for a specified prehistoric
  interval, and that every language uses recursion need qualification in a
  future substantive edition. They have not been silently corrected here.
- Pinyin, romanized Cantonese with tone numbers, and romanized Japanese
  particles preserve the language-specific grammar examples with English
  explanations. The nested-sentence examples preserve their nesting relation
  in readable English rather than mechanically copying Chinese word order.

## Pagination changes

The contributor approved pagination fixes without changing table styles.
Two back-matter tables are split at row boundaries with repeated headers:

- `latex/fragments/front004.tex`: ten recurring objects, split after the poem.
- `latex/fragments/front005.tex`: thinking tools, split after close reading.

All original rows remain, with the same `llX` column specification and booktabs
rules. The exact added boundaries are allowlisted in the structural checker.
