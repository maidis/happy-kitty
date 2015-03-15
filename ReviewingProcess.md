# Introduction #

The person who want to put his package in review and add it to Happy Kitty repository, he should be a [Happy Kitty packager](http://code.google.com/p/happy-kitty/wiki/JoiningHappyKitty#As_Happy_Kitty_Packager).

Package maintainers and the reviewers must follow the package review process and they should pay attention that the package adheres to [Pardus' Packaging Guidelines](http://developer.pardus.org.tr/guides/packaging/packaging_guidelines.html#packaging-guidelines).

They also pay attention that the package in review is not yet part of Happy Kitty literally.


# Review Process #
The package reviewing process steps on [Happy Kitty Issue Tracking System](http://code.google.com/p/happy-kitty/issues/list);
  1. When the packager thinks that his/her new package is ready for the reviewing process, he/she should copy it under the appropriate component.
```
$ pwd
/happy-kitty/game/arcade
$ svn add airstrike
$ svn ci airstrike
```
  1. If a bug is reported for requesting this new package on the bug tracking system, the process starts at this point.
  1. The developer who wants to maintain this new package, assigns the bug report to (him/her)self and changes the bug status to Accepted. This operation can only be done by the members of Committer group.
  1. After the developer assigns the bug to (him/her)self, A new bug report which will block the package request bug will be created. (From now on, this new bug report will be mentioned as the bug report)
  1. Bug report should be include "review", "package-name" (ex: airstrike), "package-component" (ex: game.arcade) tags. These tags of the bug report should be the appropriate repository component for being able to notify the relevant component responsibles by e-mail about this new package reviewing request.
  1. The Summary part of the bug report should contain the full path of the package after review folder (ex: Review: game/misc/fretsonfire). The Details part of the bug should contain the description of the package, e.g. a detailed phrase which explains the main objective of the package, what it does, etc.
  1. If the package is taken to the reviewing process because of a specific reason (e.g. the package may be a dependency of an available package in the repository or of another to-be-reviewed package), this reason should be indicated in the Details part of the bug report.
  1. If the package depends on other packages currently in reviewing process, the bug report should depend on those other packages’ bug reports to establish a dependency relationship between them.
  1. All changes done to the package during the reviewing process (e.g. All modifications committed under playground/review) should be reflected as a comment to the relevant bug report using the following special keyword in the SVN commit messages:
```

airstrike: some fixing for review

Update issue 99998

* license file added to package
* issues on 64bit build fixed
* ...
```
  1. In order to decide that the package is suitable for a package repository, it should take necessary number of approvals. The approval comments will be given firstly by the supervisor of the package component, then by an other package maintainer.
  1. In order to complete the package reviewing process 2 approval is necessary. One of these approvals should be given by component supervisor. If the package maintainer is also the component supervisor, the other package maintainers can give these two approvals.
  1. If the reviewer finds any problem about the package in review, he/she should wait for this problem to be fixed by the maintainer. In other words, the conditional approval is forbidden. Example:
```
Bad: After changing the directory paths, it will be ACK.
Good: It should change the directory paths.
```
  1. After the package maintainer has fixed the problem, the reviewer verifies the problem and gives an ACK as an approval comment.
  1. When supervisors give ACK, they will add ACKS tag to the bug. After the bug gets an ACKS it needs one more ACK from a developer. When developers give ACK, they will add ACKD tag to the bug.
  1. The package that takes the necessary approvals, the bug status is changed to Done.
  1. After the review bug report is closed, package request bug will be closed too. Done solution can also be applied for this bug. Ideally, closing both review and request bugs at the same commit is preferred.
```
Airstrike game is now part of Happy Kitty.
Thanks for your package request and package reviews.
I'm closing both package request and review issues.

Fixes issue 99998
Fixes issue 99999
```


# Resources #
  * [Pardus Developer Base - Package Reviewing Process](http://developer.pardus.org.tr/guides/packaging/package-review-process.html)
  * [Google Code - CodeReviews](http://code.google.com/p/support/wiki/CodeReviews)
  * [Google Code - IssueTracker](http://code.google.com/p/support/wiki/IssueTracker)