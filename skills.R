
skills <- rbind(c('Metatranscriptomics',95),
  c('Metagenomics',95),
  c('Mouse_models',90),
  c('Python',90),
  c('Microbial_ecology',90),
  c('Sequencing_library_prep',85),
  c('Nucleic_acid_isolation',85),
  c('Illumina_high-throughput_sequencing',80),
  c('Bash',80),
  c('R',80),
  c('Genome-scale_models',75),
  c('mothur',75),
  c('Random_forest',70),
  c('Git',70),
  c('Non-parametric/parametric_statistics',65),
  c('PBS',65),
  c('Markdown',60),
  c('Jekyll',50),
  c('MySQL/SQL',45),
  c('HTML',30),
  c('Java',20),
  c('Perl',10))

jpeg('~/Desktop/Repositories/mjenior.github.io/images/skills.jpg', quality=100, height=700, width=550)
par(mar=c(3.5,2.5,1,2))
skill_plot <- barplot(sort(as.numeric(skills[,2]), decreasing=FALSE), horiz=TRUE, las=1, xlim=c(0,100), col='black')
box()
abline(v=c(20,40,60,80), lty=2)
label_pos <- as.numeric(skills[,2]) / 2
text(label_pos, rev(skill_plot), labels=gsub('_', ' ', skills[,1]), font=2, col='white')
mtext('Novice', side=1, at=0, padj=2.5, font=2, cex=1.5)
mtext('Jedi', side=1, at=100, padj=2.5, font=2, cex=1.5)
dev.off()
