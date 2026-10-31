import { readFile } from "node:fs/promises";
import { resolve } from "node:path";
import { parseCourseInventory, type CourseInventory } from "./course";
export async function readHrmInventory(): Promise<CourseInventory> {
  try {
    const path = resolve(process.cwd(), "../../content/sydtek-learn/courses/hrm-101/course.json");
    return parseCourseInventory(JSON.parse(await readFile(path, "utf8")));
  } catch {
    return { available: false, entries: [], uniqueVideoCount: 0, capturedAt: null };
  }
}
