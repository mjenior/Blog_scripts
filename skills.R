
skills <- read.delim('~/Desktop/skills.txt', sep='\t', header=T, row.names=1)
jpeg('~/Desktop/skills.jpg', quality=100, height=700, width=550)
par(mar=c(3.5,2.5,1,2))
skill_plot <- barplot(sort(skills$Level,decreasing=FALSE), horiz=TRUE, las=1, xlim=c(0,100), col='black')
box()
abline(v=c(20,40,60,80), lty=2)
label_pos <- skills$Level/2
text(label_pos, rev(skill_plot), labels=gsub('_', ' ', rownames(skills)), font=2, col='white')
mtext('Novice', side=1, at=0, padj=2.5, font=2, cex=1.5)
mtext('Jedi', side=1, at=100, padj=2.5, font=2, cex=1.5)
dev.off()
