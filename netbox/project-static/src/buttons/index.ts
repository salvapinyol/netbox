import { initConnectionToggle } from './connectionToggle';
import { initDepthToggle } from './depthToggle';
import { initMoveButtons } from './moveOptions';
import { initPreferenceUpdate } from './preferences';
import { initReslug } from './reslug';
import { initSelectAll } from './selectAll';

export function initButtons(): void {
  for (const func of [
    initDepthToggle,
    initConnectionToggle,
    initReslug,
    initSelectAll,
    initPreferenceUpdate,
    initMoveButtons,
  ]) {
    func();
  }
}
